from django.db import models
from workstation.models import Category, Unit
from account.models import Account

# Create your models here.

class QuestionType(models.Model):
    question_type       = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__ (self):
        return self.question_type

class Questions(models.Model):
    question_title      = models.CharField(max_length=300, null=False, blank=False, unique=True)
    question_type       = models.ForeignKey(QuestionType, on_delete=models.CASCADE, null=False)
    
    def __str__ (self):
        return self.question_title

class CategoryQuestions(models.Model):
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    questions           = models.ForeignKey(Questions, on_delete=models.CASCADE, null=False)

    def __str__ (self):
        return str(self.pk)

class ScrapRecord(models.Model):
    scrap_author        = models.ForeignKey(Account, on_delete=models.CASCADE)
    scrap_unit          = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date_created        = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return str(self.pk)

class ScrapRecordToQuestion (models.Model):
    scrap_record        = models.ForeignKey(ScrapRecord, on_delete=models.CASCADE)
    question            = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer              = models.CharField(max_length=50, null=False, blank=False, default=None)

    def __str__ (self):
        return str(self.pk)


