# Generated by Django 5.0.6 on 2024-05-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_remove_newsletter_at_date_newsletter_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='start_date',
            field=models.DateTimeField(verbose_name='дата и время начала рассылки'),
        ),
    ]
