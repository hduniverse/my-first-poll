from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	 {'fields': ['question_text']}),
		('Date Informtaion', {'fields': ['pub_date']})
		]
	list_display = ('question_text', 'pub_date','was_published_recently')
	inlines = [ChoiceInLine]
	list_filter	= ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)