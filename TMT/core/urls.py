from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course, name='course'),
    path('C++Intro/', views.intro, name='intro'),
    path('C++Syntax/', views.syntax, name='syntax'),
    path('C++Varaibles/', views.varaibles, name='varaibles'),
    path('ptythonIntro/', views.pintro, name='pintro'),
    path('ptythonSyntax/', views.psyntax, name='psyntax'),
    path('ptythonVaraibles/', views.pvariables, name='pvariables'),
    path('JavaIntro/', views.jintro, name='jintro'),
    path('JavaSyntax/', views.jsyntax, name='jsyntax'),
    path('JavaVaraibles/', views.jvariables, name='jvar'),
    path('Stack/', views.Dstack, name='dstack'),
    path('Queue/', views.Dqueue, name='dqueue'),
    path('Deque/', views.Deque, name='deque'),
    path('Django Intro', views.Djintro, name='djintro'),
    path('Venv/', views.venv, name='venv'),
    path('Project/', views.project, name='project'),
    path('Http/', views.http, name='http'),
    path('Html/', views.html, name='html'),
    path('Css/', views.css, name='css'),
    path('Circular Queue/', views.circ, name='circ'),
    path('C++Output/', views.output, name='out'),
    path('pcomments/', views.comment, name='comm'),
    path('methods/', views.method, name='meth'),
    path("admin/", admin.site.urls, name='admin-site'),
]