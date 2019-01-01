from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name = "polls"
poll_urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.Signup, name='Signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.AboutPage_django, name='about'),
    url(r'^dialog/$', views.Dialog, name='dialog'),
    url(r'^MVC/$', views.MVC, name='MVC'),
    url(r'^structure/$', views.structure, name='structure'),
    url(r'^website/$', views.website, name='website'),
    url(r'^databasesupport/$', views.databasesupport, name='databasesupport'),
    url(r'^alphabet/$', views.alphabet, name='alphabet'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^hiragana/$', views.hiragana, name='hiragana'),
    url(r'^katakana/$', views.katakana, name='katakana'),
    url(r'^vocabulary/$', views.vindex, name='show'),
    url(r'^vocabulary/(?P<set_id>[0-9]+)(:show)?/?$', views.show_set, name='show'),
    url(r'^vocabulary/(?P<set_id>[0-9]+)/flip/?$', views.flip, name='flip'),
    url(r'^vocabulary/(?P<set_id>[0-9]+)/learn/?$', views.learn, name='learn'),
]
