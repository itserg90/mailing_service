import secrets

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, ListView

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserPasswordResetForm
from users.mixins import ManagerMixin
from users.models import User
from users.services import send_verification_by_email, restore_password


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_verification_by_email(user, url)
        return super().form_valid(form)


def email_verification(request, token):
    """Верифицирует пользователя, если токен совпадает"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordReset(TemplateView):
    template_name = 'users/password_reset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserPasswordResetForm()
        context['form'] = form

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        email = request.POST.get('email')
        context['email'] = email

        password = secrets.token_urlsafe(8)
        message = f'Здравствуйте! Вы запрашивали новый пароль. Ваш новый пароль: {password}'

        user = User.objects.get(email=email)
        user.password = make_password(password)
        user.save()
        restore_password(message, email)

        return render(request, 'users/password_done.html', context)


class UserPasswordDone(TemplateView):
    template_name = 'users/password_done.html'


class UserListView(LoginRequiredMixin, ManagerMixin, ListView):
    model = User


class UserUpdateView(LoginRequiredMixin, ManagerMixin, UpdateView):
    model = User
    fields = ('is_active',)
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user_list')
