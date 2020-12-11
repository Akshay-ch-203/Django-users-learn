from django.contrib import admin
from basics.models import Page, Like

# admin.site.register(Page)

# Registering using the decorator


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_info', 'date', 'user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['page_in', 'page_name',
                    'page_info', 'date', 'user', 'likes']
