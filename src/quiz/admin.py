from django.contrib import admin
from .models import (
    Category, 
    Question,
    Answer
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", 'image', 'created', 'modified',)
    search_fields = ("uuid", "name",)

class AnswerInLineModel(admin.TabularInline):
    model = Answer
    fields = ('answer', 'is_right') 

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'answer', 'is_right', 'created', 'modified',)
    list_filter = ('question',)
    search_fields = ('uuid', 'answer',)    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'question', 'level', 'created', 'modified',)
    list_filter = ('category', 'level',)
    search_fields = ('uuid', 'question',)
    inlines = (AnswerInLineModel, )

