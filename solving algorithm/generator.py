import random
import numpy as np
from numpy.lib.function_base import diff
from main2 import solve, printGrid, to2d

#generates grid with one row randomly filled --> can then use to generate full grid with solving algorithm
def generateRandomGrid():
    randomNums = [1,2,3,4,5,6,7,8,9]
    random.shuffle(randomNums) #shuffle the numbers 1-9
    randomRow = random.randint(0,8) #choose a random number to insert the numbers into
    randomGrid = []
    for i in range(9): #picks a random row to insert the random numbers, rest of grid is empty
        if i == randomRow:
            randomGrid.append(randomNums)
        else: 
            randomGrid.append([0,0,0,0,0,0,0,0,0])
    return list(np.array(randomGrid).reshape(81)) #convert to 1d list

def createPuzzle(difficulty, grid):
    solvingGrid = grid
    if difficulty == 'easy':
        minRemove = 42
        maxRemove = 47
    elif difficulty == 'medium':
        minRemove = 48
        maxRemove = 54
    else: 
        minRemove = 55
        maxRemove = 60
    numToRemove = random.randint(minRemove, maxRemove)
    removedCellPositions = []
    i = 0
    while i < numToRemove:
        position = random.randint(0,80)
        if position not in removedCellPositions:
            solvingGrid[position] = 0
            removedCellPositions.append(position)
            i += 1
    return solvingGrid

#from main2 import solve
#from grids import *

def x():
    solvedGrid = solve(generateRandomGrid())
    print('solved grid')
    print(np.array(solvedGrid).reshape(9,9))
    print('empty puzzle')
    puzzle = createPuzzle('easy', solvedGrid)
    print(np.array(puzzle).reshape(9,9))
    print('solved grid')
    print(np.array(solvedGrid).reshape(9,9))
    print('solved puzzle')
    solvedPuzzle = solve(puzzle)
    print(np.array(solvedPuzzle).reshape(9,9))

x()