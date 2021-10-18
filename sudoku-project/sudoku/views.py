from django.shortcuts import render
from django.http import HttpResponse
from sudoku.puzzles.puzzleLoader import easyPuzzles, mediumPuzzles, hardPuzzles
import random
from sudoku.puzzles.solver import solve

def index(request):
    return render(request, 'sudoku/index.html')

def gameplay(request):
    if request.method == 'GET':
        gamemode = request.GET.get('gamemode')
        if gamemode == 'easy':
            puzzle = easyPuzzles[random.randint(0,len(easyPuzzles)-1)]
        elif gamemode == 'medium':
            puzzle = mediumPuzzles[random.randint(0,len(mediumPuzzles)-1)]
        else:
            puzzle = hardPuzzles[random.randint(0,len(hardPuzzles)-1)]
        solution = solve(puzzle)
        print(puzzle)
        print(solution)
    return render(
        request, 
        'sudoku/gameplay.html', 
        {
            'gamemode':gamemode, 
            'puzzle':puzzle, 
            'solution':solution}
        )

