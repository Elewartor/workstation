from django.contrib import admin
from .models import PrintLog
 
# Register your models here.
class PrintLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'unit', 'date_printed', 'copies_printed', 'label_type')
    search_fields = [('pk')]
admin.site.register(PrintLog, PrintLogAdmin)