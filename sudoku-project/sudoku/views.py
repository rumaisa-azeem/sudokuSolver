from django.shortcuts import render
from sudoku.puzzles.puzzleLoader import easyPuzzles, mediumPuzzles, hardPuzzles
import random
import numpy as np
from sudoku.puzzles.solver import solve
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from sudoku.models import Games
from django.http import JsonResponse
from django.http import HttpResponseBadRequest, HttpResponse
import json


def index(request): # return html for index page
    return render(request, 'sudoku/index.html')

def gameplay(request): 
    if request.method == 'GET': # select a puzzle depending on which gamemode
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
        ) # return html for webpage, empty grid and solution

def stats(request): #return html for player stats page
    return render(request, 'sudoku/stats.html')


class SignUp(CreateView): # class for sign up html form
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def returnStats(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            return JsonResponse({'data':calcStats(request)}) 
            # calculate stats and return in json format
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
        # in any other case send an error


def calcStats(request): 
    games = Games.objects.filter(username_id=request.user.id) 
    easyGames = games.filter(difficulty = 'E')
    mediumGames = games.filter(difficulty = 'M')
    hardGames = games.filter(difficulty = 'H')
    # get queryset of all games played by this user from the database, 
    # then filter into easy medium and hard
    userData = { #calculate stats and put into dictionary
        'avgSolveTime': avgSolveTime(games),
        'minSolveTime': minSolveTime(games),
        'avgHintsCount': avgHintsCount(games),
        'avgSolveTime_E': avgSolveTime(easyGames),
        'minSolveTime_E': minSolveTime(easyGames),
        'avgHintsCount_E': avgHintsCount(easyGames),
        'avgSolveTime_M': avgSolveTime(mediumGames),
        'minSolveTime_M': minSolveTime(mediumGames),
        'avgHintsCount_M': avgHintsCount(mediumGames),
        'avgSolveTime_H': avgSolveTime(hardGames),
        'minSolveTime_H': minSolveTime(hardGames),
        'avgHintsCount_H': avgHintsCount(hardGames),
        'totalGames_E': len(easyGames),
        'totalGames_M': len(mediumGames),
        'totalGames_H': len(hardGames),
        'totalGames': len(games)
    }
    return userData 
    # return calculated stats dictionary to returnStats function

def avgSolveTime(gamesList): 
    solveTimeTotal = np.array([])
    for i in gamesList: # add all solve times to numpy array
        solveTimeTotal = np.append(solveTimeTotal, i.solveTime)
    if len(solveTimeTotal) == 0:
        return 'no data'
    return round(np.mean(solveTimeTotal), 0) # use numpy mean function

def minSolveTime(gamesList):
    solveTimeTotal = np.array([])
    for i in gamesList: # add all solve times to numpy array
        solveTimeTotal = np.append(solveTimeTotal, i.solveTime)
    if len(solveTimeTotal) == 0:
        return 'no data'
    return solveTimeTotal[np.argmin(solveTimeTotal)] # return smallest time

def avgHintsCount(gamesList):
    hintsTotal = np.array([])
    for i in gamesList: # add all hint counts to numpy array
        hintsTotal = np.append(hintsTotal, i.hintsCount)
    if len(hintsTotal) == 0:
        return 'no data'
    return int(round(np.mean(hintsTotal), 0))



def addGameData(request):
    print('RESULTS')
    if request.method == 'POST': 
        # take data from post request and insert into Game database object
        data = request.POST
        time = data['solveTime']
        userID = request.user.id
        hintsUsed = data['hintsCount']
        gameMode = data['gamemode']
        save = data['readytosave']
        print('solve time: ', time)
        print('user id: ', userID),
        print('hints used: ', hintsUsed),
        print('game mode: ', gameMode),
        print('ready to save: ', save)

        if save == 'true': 
        # if the data is ready to save (user has submitted a correct grid)
            game = Games(
                username=User.objects.get(id=userID), 
                solveTime=time, 
                hintsCount=hintsUsed, 
                difficulty=gameMode
                )
            game.save() # save data to database

    return HttpResponse()
    