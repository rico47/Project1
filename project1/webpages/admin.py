from django.contrib import admin
from .models import Webpage, Stats


@admin.register(Webpage)
class WebpageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'idx_js', 'idx_html', 'idx_bool']

