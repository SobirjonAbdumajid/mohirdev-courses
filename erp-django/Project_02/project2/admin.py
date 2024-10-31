from django.contrib import admin

from .models import Teacher, Experience, TeacherInfo

admin.site.register(Teacher)
admin.site.register(Experience)
admin.site.register(TeacherInfo)