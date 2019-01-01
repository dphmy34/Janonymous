from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Video, Lesson,Card

admin.site.register(Video)
admin.site.register(Lesson)
admin.site.register(Card)

