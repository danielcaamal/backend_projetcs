from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.StackedInline):
    model = Choice
    fields = ['text']
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','text']
    inlines = [ChoiceInLine]
    list_display = ('text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['text']
    


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
