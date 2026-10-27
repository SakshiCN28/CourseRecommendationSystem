from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    skills = models.TextField()
    duration = models.CharField(max_length=100)
    description = models.TextField()
    career_field = models.CharField(max_length=150)

    def __str__(self):
        return self.course_name