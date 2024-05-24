from django.urls import path
from mailing.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, \
    NewsletterDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, AttemptListView
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/update/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/<int:pk>/delete/', NewsletterDeleteView.as_view(), name='newsletter_delete'),

    path('messages', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('clients', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('attempts', AttemptListView.as_view(), name='attempt_list'),
]
