# Generated by Django 5.0.6 on 2024-05-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_alter_newsletter_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название рассылки'),
        ),
    ]
