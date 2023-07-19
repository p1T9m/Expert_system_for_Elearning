from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def course(request):
    return render(request, 'core/course.html')

def intro(request):
    return render(request, 'core/c++intro.html')



