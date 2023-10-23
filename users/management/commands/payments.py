from typing import Iterable

from django.core.management.base import BaseCommand
from users.models import Payment, User


class Command(BaseCommand):
    help = 'Заполнение данных о платежах'
    requires_migrations_checks = True
    fixtures: Iterable[str] = ('payment_data.json',)

    def handle(self, *args, **kwargs):
        payment_data = [
            {
                'user': User.objects.all().first(),
                'payment_date': '2022-01-01',
                'paid_course_or_lesson': 'Course 1',
                'payment_amount': 100.00,
                'payment_method': 'cash',
            },
            {
                'user': User.objects.all().first(),
                'payment_date': '2022-01-02',
                'paid_course_or_lesson': 'Course 2',
                'payment_amount': 150.00,
                'payment_method': 'transfer',
            },
        ]

        for data in payment_data:
            Payment.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Данные о платежах успешно заполнены'))