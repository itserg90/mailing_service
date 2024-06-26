# Generated by Django 5.0.6 on 2024-05-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_remove_newsletter_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='at_date',
            field=models.DateTimeField(verbose_name='дата и время первой отправки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('launched', 'запущена'), ('finished', 'завершена')], default='created', max_length=100, verbose_name='статус'),
        ),
    ]
