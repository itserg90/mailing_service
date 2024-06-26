from django.urls import path

from mailing import views
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('newsletters', views.NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', views.NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', views.NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/update/', views.NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/<int:pk>/delete/', views.NewsletterDeleteView.as_view(), name='newsletter_delete'),

    path('messages', views.MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', views.MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message_delete'),

    path('clients', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),

    path('attempts', views.AttemptListView.as_view(), name='attempt_list'),
]
