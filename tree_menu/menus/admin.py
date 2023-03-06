from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'parent',
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('title',),
    }
