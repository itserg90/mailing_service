from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.mixins import StyleFormMixin


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserPasswordResetForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
