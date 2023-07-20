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

def syntax(request):
    return render(request, 'core/c++syntax.html')

def varaibles(request):
    return render(request, 'core/c++varaibles.html')

def pintro(request):
    return render(request, 'core/pythonintro.html')

def psyntax(request):
    return render(request, 'core/pythonsyntax.html')

def pvariables(request):
    return render(request, 'core/pythonvariable.html')

def jintro(request):
    return render(request, 'core/Javaintro.html')

def jsyntax(request):
    return render(request, 'core/Javasyntax.html')

def jvariables(request):
    return render(request, 'core/Javavar.html')



