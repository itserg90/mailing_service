from random import shuffle

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog
from mailing.forms import NewsletterForm, StatusNewsletterForm
from mailing.mixins import UserAutofillMixin, OwnerMixin, OwnerManagerMixin, KwargsMixin, NotManagerMixin
from mailing.models import Newsletter, Message, Client, Attempt


def home_page(request):
    """Главная страница"""
    data = {'data_list': [], 'blog': []}
    newsletters = Newsletter.objects.filter(user=request.user.id)
    data['data_list'].append(f'Количество рассылок всего: {len(newsletters)}')
    data['data_list'].append(
        f'Количество активных рассылок: {len([obj for obj in newsletters if obj.status == "Запущена"])}')
    data['data_list'].append(
        f'Количество уникальных клиентов для рассылок: {len(Client.objects.filter(user=request.user.id))}')

    # Получаем 3 случайные статьи
    blog = list(Blog.objects.all())
    shuffle(blog)
    data['blog'].extend(blog[:3])

    return render(request, 'mailing/home_page.html', data)


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, OwnerManagerMixin, DetailView):
    model = Newsletter

    def get_form_class(self):
        if not self.request.user == self.object.user:
            raise PermissionDenied

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


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
        if user.has_perms(['mailing.can_disable_status', 'mailing.view_newsletter']):
            return StatusNewsletterForm
        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, OwnerMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_published=True)


class MessageDetailView(LoginRequiredMixin, OwnerMixin, DetailView):
    model = Message

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


class MessageCreateView(LoginRequiredMixin, NotManagerMixin, UserAutofillMixin, CreateView):
    model = Message
    # form_class = MessageForm
    fields = ['subject', 'text']
    success_url = reverse_lazy('mailing:message_list')

    # def form_valid(self, form):
    #     obj = form.save()
    #     newsletter_mail(obj)
    #     return super().form_valid(form)


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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_published=True)


class ClientDetailView(LoginRequiredMixin, OwnerMixin, DetailView):
    model = Client

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


class ClientCreateView(LoginRequiredMixin, NotManagerMixin, UserAutofillMixin, CreateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailing:client_list')

    # def form_valid(self, form):
    #     obj = form.save()
    #     newsletter_mail(obj)
    #     return super().form_valid(form)


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
