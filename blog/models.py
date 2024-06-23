from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(verbose_name='просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
