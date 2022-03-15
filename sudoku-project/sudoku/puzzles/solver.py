import numpy as np
from sudoku.puzzles.cellClass import Cell
from sudoku.puzzles.sets import *

def generateGrid(gridVals):
    grid = []
    for i in range(81):
        grid.append (Cell(i//9, i%9, gridVals[i]))
    return grid

def to2d(grid):
    return np.array(grid).reshape(9,9)

def percentComplete(grid):
    j = 0
    for i in range(81):
        if grid[i].val != 0:
            j+=1
    num = (round(j/81*100))
    return num

def blanksPerSet(grid2d):
    blanks = []
    for i in range(9):
        blanksInSet = 0
        for j in range(9):
            if grid2d[allSets[i][j][0]][allSets[i][j][1]].val == 0:
                blanksInSet += 1
        
        if blanksInSet == 0:
            blanks.append(10)
        else:
            blanks.append(blanksInSet)

    return blanks

def findNextBlanks(grid2d):
    nextSet = allSets[np.argmin(blanksPerSet(grid2d))]
    x =[]
    for i in range(9):
        if grid2d[nextSet[i][0]][nextSet[i][1]].val == 0:
            x.append(nextSet[i])
    return x


############################################################################# main solving function

def solve(givenGrid): #takes a 1d list of numbers as the grid
    #create a list of objects to represent 81 cells in the 9x9 grid   
    grid = generateGrid(givenGrid) 
    grid2d = to2d(grid)

    singleValidNumFound = True
    j = 1
    
    #find valid numbers for each cell
    while singleValidNumFound:
        singleValidNumFound = False
        for i in range(81):
            grid[i].findValidNums(grid2d)
            if len(grid[i].validNums) == 1:
                singleValidNumFound = True
                grid[i].setVal(grid[i].validNums[0]) 
            grid[i].resetValidNums()
        j+=1

    nextBlanks = findNextBlanks(grid2d) #the queue of the next cells to look at and consider the solutions for

    editedCells = []
    run = True
    count = 0

    while run:
        if len(nextBlanks) > 0:
            count+=1
            cell = grid2d[nextBlanks[0][0]][nextBlanks[0][1]]
            if cell.val == 0:
                cell.findValidNums(grid2d)
            if len(cell.validNums) > 0:
                cell.setVal(cell.validNums.pop(0))
                editedCells.append(nextBlanks.pop(0))
            else: 
                cell.setVal(0)
                nextBlanks = [editedCells.pop()]

        else:
            nextBlanks = findNextBlanks(grid2d)
            if percentComplete(grid) == 100:
                run = False

    solution = []

    for i in range(81):
        solution.append(grid[i].val) #convert grid of objects to list of just values

    return solution
