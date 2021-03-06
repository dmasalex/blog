# Generated by Django 4.0 on 2022-01-05 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My blog!', max_length=255, verbose_name='Тема поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тема поста'),
        ),
    ]
