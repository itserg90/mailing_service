import smtplib
from datetime import datetime, timedelta
from pytz import timezone

from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from mailing.models import Newsletter, Attempt


def send_newsletter(obj):
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
    if obj.status == 'создана':
        obj.status = 'запущена'
        obj.save()


def newsletter_mail():
    """
    Функция отправки рассылки
    """
    zone = timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    for obj in Newsletter.objects.filter(status__in=('создана', 'запущена')):
        if obj.start_date < current_datetime < obj.end_date:
            attempt = Attempt.objects.filter(newsletter=obj)
            if attempt.exists():
                last_date = attempt.order_by('at_date').last()
                current_timedelta = current_datetime - last_date
                if current_timedelta <= timedelta(days=1) and obj.periodicity == 'ежедневно':
                    send_newsletter(obj)
                elif current_timedelta >= timedelta(days=7) and obj.periodicity == 'еженедельно':
                    send_newsletter(obj)
                elif current_timedelta >= timedelta(days=30) and obj.periodicity == 'ежемесячно':
                    send_newsletter(obj)
            else:
                send_newsletter(obj)
