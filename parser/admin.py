from django.contrib import admin

from parser.models import Ranobe, RanobeFile


@admin.register(Ranobe)
class RanobeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    sortable_by = ('id', 'title',)
    list_per_page = 10


@admin.register(RanobeFile)
class RanobeFileAdmin(admin.ModelAdmin):
    list_display = ('ranobe', 'file')
    list_filter = ('ranobe',)
    list_per_page = 10
