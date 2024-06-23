from django import forms

from mailing.mixins import UserAutofillMixin
from mailing.models import Client, Newsletter, Message


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'start_date', 'end_date', 'periodicity', 'clients', 'message', 'status']

    def __init__(self, *args, **kwargs):
        """Переопределяет поля(клиенты, сообщение) с учетом фильтрации по пользователю"""
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(user=user)
        self.fields['message'].queryset = Message.objects.filter(user=user)


class StatusNewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('status',)

    def __init__(self, *args, **kwargs):
        """Удаляем лишний словарь, он нужен для другой формы"""
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['subject', 'text']
