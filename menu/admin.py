from django.contrib import admin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'title')
    ordering = ('name', 'parent__id', 'id')
