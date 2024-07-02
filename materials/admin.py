from django.contrib import admin

from materials.models import LearningCourse, Lesson


@admin.register(LearningCourse)
class LearningCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'imagery',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'course', 'imagery', 'video',)
    list_filter = ('course',)
    search_fields = ('name', 'description',)
