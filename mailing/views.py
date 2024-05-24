from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Newsletter, Message, Client, Attempt


class NewsletterListView(ListView):
    model = Newsletter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_published=True)


class NewsletterDetailView(DetailView):
    model = Newsletter

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ['start_date', 'end_date', 'periodicity', 'clients', 'message']
    success_url = reverse_lazy('mailing:newsletter_list')

    # def form_valid(self, form):
    #     obj = form.save()
    #     newsletter_mail(obj)
    #     return super().form_valid(form)


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ['start_date', 'end_date', 'periodicity', 'clients', 'message']

    def get_success_url(self):
        return reverse('mailing:newsletter_detail', args=[self.kwargs.get('pk')])


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailing:newsletter_list')


class MessageListView(ListView):
    model = Message

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_published=True)


class MessageDetailView(DetailView):
    model = Message

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'text']
    success_url = reverse_lazy('mailing:message_list')

    # def form_valid(self, form):
    #     obj = form.save()
    #     newsletter_mail(obj)
    #     return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'text']

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class ClientListView(ListView):
    model = Client

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_published=True)


class ClientDetailView(DetailView):
    model = Client

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailing:client_list')

    # def form_valid(self, form):
    #     obj = form.save()
    #     newsletter_mail(obj)
    #     return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'comment']

    def get_success_url(self):
        return reverse('mailing:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class AttemptListView(ListView):
    model = Attempt
