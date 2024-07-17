from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(PDF)
admin.site.register(Quiz)
admin.site.register(Enrollment)
admin.site.register(ChildProgress)