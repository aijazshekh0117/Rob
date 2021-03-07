from django.contrib import admin

# Register your models here.


from .models.questions import Question
from .models import Answer
from .models import Role


class QuestionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionsAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)
