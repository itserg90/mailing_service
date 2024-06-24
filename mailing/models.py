from django.db import models

from users.models import User


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рассылки', null=True, blank=True, default='Рассылка')
    start_date = models.DateTimeField(verbose_name='дата и время начала рассылки')
    end_date = models.DateTimeField(verbose_name='дата и время окончанмя рассылки', null=True, blank=True)
    periodicity = models.CharField(max_length=100, verbose_name='периодичность', default='Ежедневно',
                                   choices=(('Ежедневно', 'Ежедневно'),
                                            ('Еженедельно', 'Еженедельно'),
                                            ('Ежемесячно', 'Ежемесячно')))
    status = models.CharField(max_length=100, verbose_name='статус', default='Создана',
                              choices=(('Создана', 'Создана'),
                                       ('Запущена', 'Запущена'),
                                       ('Завершена', 'Завершена')))

    clients = models.ManyToManyField(Client, blank=True, related_name='clients', verbose_name='Клиенты')
    message = models.OneToOneField('Message', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='message', verbose_name='Сообщение')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('can_disable_newsletter', 'Can disable newsletter')
        ]


class Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.subject}: {self.text}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Attempt(models.Model):
    at_date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    is_success = models.BooleanField(default=False, verbose_name='успешность попытки')
    server_response = models.TextField(default=False, verbose_name='ответ сервера')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='newsletter')

    def __str__(self):
        return f'{self.at_date}: {self.is_success}'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
