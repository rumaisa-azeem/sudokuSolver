from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'sudoku/index.html')

def gameplay(request):
    return render(request, 'sudoku/gameplay.html')