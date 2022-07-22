from django.contrib import admin
from .models import Webpage, Stats


class StatsInLine(admin.StackedInline):
    model = Stats


@admin.register(Webpage)
class WebpageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['title']
    sortable_by = ['title']
    search_fields = ['title']
    inlines = [
        StatsInLine,
    ]

    def getimage_from_url(self, str_url):
        pass


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'idx_js', 'idx_html', 'idx_bool']
