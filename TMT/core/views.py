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

def Dstack(request):
    return render(request, 'core/dstack.html')

def Dqueue(request):
    return render(request, 'core/dqueue.html')

def Deque(request):
    return render(request, 'core/deque.html')

def http(request):
    return render(request, 'core/http.html')

def html(request):
    return render(request, 'core/html.html')

def css(request):
    return render(request, 'core/css.html')

def Djintro(request):
    return render(request, 'core/djintro.html')

def venv(request):
    return render(request, 'core/venv.html')

def project(request):
    return render(request, 'core/project.html')

def circ(request):
    return render(request, 'core/circular.html')

def output(request):
    return render(request, 'core/c++output.html')

def comment(request):
    return render(request, 'core/pcomments.html')

def method(request):
    return render(request, 'core/methods.html')



