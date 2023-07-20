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
    path("admin/", admin.site.urls, name='admin-site'),
]