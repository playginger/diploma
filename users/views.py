from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, LoginForm, PostForm, SubscriptionForm
from django.contrib.auth import authenticate, login
from .models import Post
import stripe
from django.conf import settings
from stripe import error


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            url = reverse('users:view_post', kwargs={"post_id": post.id})
            return redirect(url)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def view_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'view_post.html', {'post': post})


stripe.api_key = settings.STRIPE_SECRET_KEY


def process_payment(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Получите данные из формы
            credit_card_number = form.cleaned_data['credit_card_number']
            expiration_date = form.cleaned_data['expiration_date']
            cvv = form.cleaned_data['cvv']

            # Stripe API для обработки платежа
            try:
                charge = stripe.Charge.create(
                    amount=1000,  # Сумма платежа
                    currency='usd',
                    source=credit_card_number,
                    description='Subscription payment'
                )
                # Платеж успешно обработан
                return render(request, 'payment_success.html')
            except stripe.error.CardError:
                # Ошибка обработки платежа
                return render(request, 'payment_error.html')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription.html', {'form': form})
