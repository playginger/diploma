from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='dicks',
            is_staff=True,
            is_superuser=True,
            phone_number='800885544666',

        )

        user.set_password('123qwe456rty')
        user.save()
