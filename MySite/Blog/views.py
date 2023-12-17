from django.shortcuts import render

def Home(request):
    return render(request, 'Blog/home.html')

def About(request):
    return render(request, 'Blog/about.html')