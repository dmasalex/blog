from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Категория"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Post(models.Model):
    """Блог"""

    title = models.CharField('Тема поста', max_length=255)
    title_tag = models.CharField('Заголовок', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField('Дата создания', auto_now_add=True)
    #body = models.TextField('Текст поста')
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']

