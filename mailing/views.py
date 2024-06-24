from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import NewsletterForm, StatusNewsletterForm
from mailing.mixins import UserAutofillMixin, OwnerMixin, OwnerManagerMixin, KwargsMixin, NotManagerMixin
from mailing.models import Newsletter, Message, Client, Attempt
from mailing.services import get_three_articles, get_newsletters


def home_page(request):
    """Главная страница"""
    data = {'newsletters': '', 'active_newsletters': '', 'clients': '', 'blog': []}

    data['newsletters'], data['active_newsletters'], data['clients'] = get_newsletters(request, data)

    data['blog'] = get_three_articles(data)

    return render(request, 'mailing/home_page.html', data)


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    ordering = 'user'


class NewsletterDetailView(LoginRequiredMixin, OwnerManagerMixin, DetailView):
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, NotManagerMixin, UserAutofillMixin, KwargsMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailing:newsletter_list')


class NewsletterUpdateView(LoginRequiredMixin, OwnerManagerMixin, KwargsMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    # fields = ['start_date', 'end_date', 'periodicity', 'clients', 'message', 'status']

    def get_success_url(self):
        return reverse('mailing:newsletter_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return NewsletterForm
        if user.has_perms(['mailing.can_disable_newsletter', 'users.can_disable_user']):
            return StatusNewsletterForm
        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, OwnerMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, NotManagerMixin, UserAutofillMixin, CreateView):
    model = Message
    fields = ['subject', 'text']
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    model = Message
    fields = ['subject', 'text']

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, OwnerMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, NotManagerMixin, UserAutofillMixin, CreateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    model = Client
    fields = ['name', 'email', 'comment']

    def get_success_url(self):
        return reverse('mailing:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
