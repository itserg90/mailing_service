from django.contrib import admin
from django.forms import modelform_factory

from mailing.models import Newsletter, Message, Client, Attempt


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'periodicity', 'start_date', 'end_date', 'status', 'user')
    list_filter = ('periodicity', 'start_date', 'end_date', 'status')
    search_fields = ('periodicity', 'start_date', 'end_date', 'status')
    readonly_fields = ('status',)
    ordering = ('periodicity', 'start_date', 'end_date', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'text', 'user')
    search_fields = ('subject',)
    ordering = ('subject',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment', 'user')
    search_fields = ('name', 'email',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'newsletter', 'at_date', 'is_success',)
