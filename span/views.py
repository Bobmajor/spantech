from django.shortcuts import render

def index(request):
    return render(request, 'span/index.html')

def about(request):
    return render(request, 'span/about.html')

def services(request):
    return render(request, 'span/services.html')

def team(request):
    return render(request, 'span/team.html')

def fqa(request):
    return render(request, 'span/error.html')