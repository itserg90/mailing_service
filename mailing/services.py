from random import shuffle

from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED
from mailing.models import Newsletter, Client


def get_three_articles(data):
    """Получает три случайные статьи из кэша, если там нет, то из базы данных"""

    def get_blog():
        """Получает список статей из базы данных"""
        blog = list(Blog.objects.all())
        shuffle(blog)
        return blog[:3]

    if not CACHE_ENABLED:
        data['blog'] = get_blog()
    else:
        key_blog = 'blogs'
        blogs = cache.get(key_blog)
        if blogs is not None:
            data['blog'] = blogs
        else:
            data['blog'] = get_blog()
            cache.set(key_blog, data['blog'])
    return data['blog']


def get_newsletters(request, data):
    """Получает количество рассылок и клиентов из кэша, если там нет, то из базы данных"""

    def get_newsletter():
        """Получает количество рассылок и клиентов из базы данных"""
        current_newsletters = Newsletter.objects.filter(user=request.user.id)
        data['newsletters'] = f'Количество рассылок всего: {len(current_newsletters)}'
        data['active_newsletters'] = (f'Количество активных рассылок: '
                                      f'{len([obj for obj in current_newsletters if obj.status == "Запущена"])}')

        data['clients'] = (f'Количество уникальных клиентов для рассылок: '
                           f'{len(Client.objects.filter(user=request.user.id))}')
        return data

    if not CACHE_ENABLED:
        return get_newsletter()
    else:
        key_newsletter, key_active_newsletters, key_clients = 'newsletters', 'active_newsletters', 'clients'

        newsletters = cache.get(key_newsletter)
        active_newsletters = cache.get(key_active_newsletters)
        clients = cache.get(key_clients)

        if newsletters is not None:
            data['newsletters'] = newsletters
        else:
            cache.set(key_newsletter, get_newsletter()['newsletters'])

        if active_newsletters is not None:
            data['active_newsletters'] = active_newsletters
        else:
            cache.set(key_active_newsletters, get_newsletter()['active_newsletters'])

        if clients is not None:
            data['clients'] = clients
        else:
            cache.set(key_clients, get_newsletter()['clients'])

        return data['newsletters'], data['active_newsletters'], data['clients']
