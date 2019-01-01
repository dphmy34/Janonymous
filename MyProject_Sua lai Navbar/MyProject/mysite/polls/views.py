from random import randrange

from django.core import serializers
from django.forms import formset_factory
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
# from .forms import UserForm, LoginForm
from .forms import UserForm, CardForm, LessonForm
from .models import Video, Lesson, Card

all_sets = {}
current_cards = {}
current_set_id = -1
empty_card_index = 0
admin = False


# Showing the vocabulary page
def vindex(request):
    global all_sets
    all_sets = Lesson.objects.all()
    set_lens = []
    for set in all_sets:
        # Subtract one from the length for the empty card.
        set_lens.append(len(set.card_set.all()) - 1)

    return render(request, 'Flashcards\index.html', {'all_sets': all_sets, 'set_lens': set_lens, 'admin': admin})


def show_set(request, set_id):
    global all_sets, current_cards, current_set_id
    lesson = Lesson.objects.get(id=set_id)
    current_cards = lesson.card_set.all()
    # current_cards = Card.objects.all()
    title = lesson.name
    current_set_id = set_id

    return render(request, 'Flashcards\set.html', {
        'set_id': set_id, 'cards': current_cards, 'title': title, 'empty_card_index': 0, 'admin': admin
    })


def flip(request, set_id):
    flashcards = serializers.serialize("json", Lesson.objects.get(id=set_id).card_set.all())
    return render(request, 'Flashcards/flip.html', {
        'cards': flashcards, 'set_id': set_id, 'admin': admin
    })


def learn(request, set_id):
    flashcards_data = Lesson.objects.get(id=set_id)
    flashcards = serializers.serialize("json", flashcards_data.card_set.all())
    return render(request, 'Flashcards/learn.html', {
        'title': flashcards_data.name, 'cards': flashcards, 'set_id': set_id, 'admin': admin
    })


def index(request):
    query = request.GET.get("q")
    if query:

        return render(request, 'Login/base_visitor.html')
    else:
        return render(request, 'Login/base_visitor.html')


def Signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/home.html')
    context = {
        "form": form,
    }
    return render(request, 'Login/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Q&A/home.html')
            else:
                return render(request, 'Login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Login/login.html')


def logout(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, "Login/login.html", context)

# def test(request):
#     return render(request, 'test.html')

def home(request):
    return render(request, 'home/home.html')


def AboutPage_django(request):
    return render(request, 'home/about.html')


def Dialog(request):
    list_video = Video.objects.all()
    context = {'list_video': list_video}
    return render(request, 'Japanese/dialog.html', context)


def MVC(request):
    return render(request, 'Q&A/MVC.html')


def structure(request):
    return render(request, 'Q&A/structure.html')


def website(request):
    return render(request, 'Q&A/website.html')


def databasesupport(request):
    return render(request, 'Q&A/databasesupport.html')


def alphabet(request):
    return render(request, 'Japanese/alphabet.html')


def compare(request):
    return render(request, 'Q&A/compare.html')


def hiragana(request):
    return render(request, 'Japanese/hiragana.html')


def katakana(request):
    return render(request, 'Japanese/katakana.html')


