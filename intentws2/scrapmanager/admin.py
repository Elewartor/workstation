from django.contrib import admin
from scrapmanager.models import QuestionType, Questions, CategoryQuestions, ScrapRecord, ScrapRecordToQuestion
# Register your models here.

admin.site.register(QuestionType)
admin.site.register(Questions)
admin.site.register(CategoryQuestions)
admin.site.register(ScrapRecordToQuestion)

class ScrapRecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'scrap_author', 'scrap_unit', 'date_created',)
    search_fields = [('pk')]

admin.site.register(ScrapRecord, ScrapRecordAdmin)