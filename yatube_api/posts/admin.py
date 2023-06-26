from django.contrib import admin
from django.db import models
from django.forms import Textarea
from posts.models import Comment, Group, Post


class ViewSettings(admin.ModelAdmin):
    list_per_page = 10
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 45})},
    }


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(ViewSettings):
    list_display = (
        'post', 'author', 'text',
        'created'
    )
    list_editable = (
        'text',
    )
    search_fields = ('post', 'author', 'created')
    list_filter = ('created', 'author', 'post')
    empty_value_display = 'Не задано'


class GroupAdmin(ViewSettings):
    list_display = (
        'title', 'slug', 'description'
    )
    list_editable = (
        'description', 'slug'
    )
    search_fields = (
        'title', 'description', 'slug'
    )
    list_filter = (
        'title', 'description', 'slug'
    )
    empty_value_display = 'Не задано'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
