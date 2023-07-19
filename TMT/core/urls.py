from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course, name='course'),
    path('C++intro/', views.intro, name='intro'),
    path("admin/", admin.site.urls, name='admin-site'),
]