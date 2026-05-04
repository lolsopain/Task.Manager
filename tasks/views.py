from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def easy(request):
    tasks = [
        {"title": "Print Hello World", "desc": "Use print()"},
        {"title": "Variables", "desc": "Store values in variables"},
        {"title": "Basic Math", "desc": "Use +, -, *, /"},
        {"title": "Input", "desc": "Get user input"},
        {"title": "If statements", "desc": "Learn conditions"},
    ]
    return render(request, 'easy.html', {"tasks": tasks})


def medium(request):
    tasks = [
        {"title": "Loops Practice", "desc": "Print numbers 1–100"},
        {"title": "Even or Odd", "desc": "Check number type"},
        {"title": "List Manager", "desc": "Add/remove list items"},
        {"title": "Functions", "desc": "Create reusable code"},
        {"title": "Calculator", "desc": "Build simple calculator"},
    ]
    return render(request, 'medium.html', {"tasks": tasks})


def hard(request):
    tasks = [
        {"title": "Todo CLI App", "desc": "Command-line task manager"},
        {"title": "File Handling", "desc": "Read/write files"},
        {"title": "Password Generator", "desc": "Generate secure passwords"},
        {"title": "API Fetch", "desc": "Get data from API"},
        {"title": "Mini Game", "desc": "Number guessing game"},
    ]
    return render(request, 'hard.html', {"tasks": tasks})