# Generated by Django 4.2.2 on 2024-06-20 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0011_alter_newsletter_clients_alter_newsletter_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='Клиенты', to='mailing.client', verbose_name='Клиенты'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Сообщение', to='mailing.message', verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='name',
            field=models.CharField(blank=True, default='Рассылка', max_length=100, null=True, verbose_name='Название рассылки'),
        ),
    ]
