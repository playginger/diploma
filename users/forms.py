from django import forms
from .models import User, Post


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class SubscriptionForm(forms.Form):
    credit_card_number = forms.CharField(label='Credit Card Number')
    expiration_date = forms.CharField(label='Expiration Date')
    cvv = forms.CharField(label='CVV')
