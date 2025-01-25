from django.contrib import admin
from .models import CsvFile

class CsvFileAdmin(admin.ModelAdmin):
    list_display = ('username', 'csv_file', 'created')

admin.site.register(CsvFile)