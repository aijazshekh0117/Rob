from django.contrib import admin

# Register your models here.


from .models.questions import Question


class QuestionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionsAdmin)
