from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')  # Add this decorator to require authentication
def second_expert(request):
    if request.method == 'GET':
        proficiency_level = request.GET.get('proficiency_level')
        if proficiency_level == 'beginner':
            return redirect('beginner')
        elif proficiency_level == 'intermediate':
            return redirect('inter')
        elif proficiency_level == 'advanced':
            return redirect('advanced')
    return render(request, 'second_expert/second_expert.html')

@login_required(login_url='/login/')  # Add this decorator to require authentication
def beginner(request):
    # Perform logic specific to the beginner page
    introduction = " test Based on your level you should start with python or C++ as their syntax is easy to learn. this will make your application simpler and more powerful and more flexible."
    context = {
        'introduction': introduction,
    }
    return render(request, 'second_expert/beginner.html', context)

@login_required(login_url='/login/')  # Add this decorator to require authentication
def inter(request):
    # Perform logic specific to the intermediate page
    introduction = "Study object-oriented programming concepts and data structures and algorithms. This will help your skills become more advanced."
    context = {
        'introduction': introduction,
    }
    return render(request, 'second_expert/inter.html', context)

@login_required(login_url='/login/')  # Add this decorator to require authentication
def advanced(request):
    # Perform logic specific to the advanced page
    introduction = "I will provide you with two frameworks. If you're more into backend, go with Django. If you prefer frontend, go with web development."
    context = {
        'introduction': introduction,
    }
    return render(request, 'second_expert/advanced.html', context)
