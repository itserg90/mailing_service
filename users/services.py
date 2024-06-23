from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_verification_by_email(user, url):
    """Отправляет верификацию на почту"""
    send_mail(
        subject="Подтверждение почты",
        message=f"Здравствуйте! Пожалуйста, перейдите по ссылке для подтверждения почты {url}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email]
    )


def restore_password(message, email):
    """Отправляет на почту новый пароль"""
    send_mail(
        subject="Восстановление пароля",
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[email]
    )
