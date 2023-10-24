from .apps import UsersConfig

from django.urls import path
from .views import registration_view, login_view, create_post_view, view_post_view

app_name = UsersConfig.name
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('create/', create_post_view, name='create_post'),
    path('post/<int:post_id>/', view_post_view, name='view_post'),
]
