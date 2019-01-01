from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Lesson,Card


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password')

class LessonForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput, label='')
    color = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Lesson
        fields = ['name']


class CardForm(forms.ModelForm):
    front = forms.CharField(widget=forms.TextInput, label='')
    back = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Card
        fields = ['front', 'back']


