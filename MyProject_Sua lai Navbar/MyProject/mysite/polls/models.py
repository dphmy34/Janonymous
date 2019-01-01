from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Lesson (models.Model):
    name = models.CharField(max_length= 256)
    def __str__(self):
        return self.name
class Card (models.Model):
    Lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    front_jap = models.CharField(max_length= 256)
    back_eng = models.CharField(max_length=256, default= 'Null')
   # audio = models.FileField(upload_to='./static/polls/audio', default= 'mơ/mysite/polls/static/polls/audio/Death1.wav')
    def __str__(self):
        return self.front_jap+", "+self.back_eng


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text



class Video(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    time = models.DateTimeField()
    def __str__(self):
        return self.title




