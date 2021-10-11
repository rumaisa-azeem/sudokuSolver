from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'sudoku/index.html')

def gameplay(request):
    if request.method == 'GET':
        gamemode = request.GET.get('gamemode')
        puzzle = []
        solution = []

    return render(
        request, 
        'sudoku/gameplay.html', 
        {
            'gamemode':gamemode, 
            'puzzle':puzzle, 
            'solution':solution}
        )

