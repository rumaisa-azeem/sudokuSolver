from django.shortcuts import render
from sudoku.puzzles.puzzleLoader import easyPuzzles, mediumPuzzles, hardPuzzles
import random
from sudoku.puzzles.solver import solve
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


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

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'