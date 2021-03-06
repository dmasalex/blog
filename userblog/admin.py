from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'body')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
