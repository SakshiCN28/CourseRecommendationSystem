from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category', 'level', 'duration', 'career_field')
    search_fields = ('course_name', 'category', 'skills', 'career_field')
    list_filter = ('category', 'level')