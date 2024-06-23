from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password-reset/', UserPasswordReset.as_view(), name='password_reset'),
    path('password-done/', UserPasswordDone.as_view(), name='password_done'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
]
