from django.contrib import admin

from . import models

class LJTTCardAdmin(admin.ModelAdmin):
    list_display = ('jp_word', 'en_word', 'en_pronounciation',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('lessonName',) 


admin.site.register(models.LJTTCard, LJTTCardAdmin)
admin.site.register(models.Lesson, LessonAdmin)
