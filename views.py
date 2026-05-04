from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def easy(request):
    return render(request, 'easy.html')

def medium(request):
    return render(request, 'medium.html')

def hard(request):
    return render(request, 'hard.html')