import smtplib
from datetime import datetime

from django.core.mail import send_mail
from pytz import timezone

from config import settings
from mailing.models import Newsletter, Attempt

from django.core.management import BaseCommand
from config.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    def handle(self, *args, **options):
        def newsletter_mail():
            """
            Функция отправки рассылки
            """
            zone = timezone(settings.TIME_ZONE)
            current_datetime = datetime.now(zone)
            for obj in Newsletter.objects.filter(status__in=('создана', 'запущена')):
                if obj.start_date < current_datetime < obj.end_date:
                    try:
                        server_response = send_mail(
                            f'{obj.message.subject}',
                            f'{obj.message.text}',
                            EMAIL_HOST_USER,
                            recipient_list=[client.email for client in obj.clients.all()],
                            fail_silently=False,
                        )
                        a = Attempt.objects.create(newsletter=obj, server_response=server_response)
                        a.is_success = True
                        a.save()
                    except smtplib.SMTPException as e:
                        Attempt.objects.create(newsletter=obj, server_response=e)

        newsletter_mail()
