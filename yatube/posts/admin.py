from django.contrib import admin
from .models import Post, Group
# from yatube.yatube.settings import EMPTY
from django.conf import settings


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )

    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY


admin.site.register(Group)