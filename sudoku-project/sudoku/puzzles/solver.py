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
    return round(j/81*100)

def blanksPerSet(grid2d):
    blanks = []
    for i in range(9):
        blanksInSet = 0
        for j in range(9):
            if grid2d[allSets[i][j][0]][allSets[i][j][1]].val == 0:
                blanksInSet += 1
        
        if blanksInSet == 0:
            blanks.append(10)
        #if the set is completely full then set its number to 10 so it isn't considered by np.argmin

        else:
            blanks.append(blanksInSet)

    return blanks

def findNextBlanks(grid2d):
    nextSet = allSets[np.argmin(blanksPerSet(grid2d))] #returns the set with the least blank cells to solve next
    coOrds =[]
    for i in range(9):
        if grid2d[nextSet[i][0]][nextSet[i][1]].val == 0:
            coOrds.append(nextSet[i])
    return coOrds #returns a list of co-ordinates of the blank cells in the next set


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

    nextBlanks = findNextBlanks(grid2d) #the queue of the next cells  co-ordinates to look at and consider the solutions for

    editedCells = []
    run = True
    count = 0

    while run:
        if len(nextBlanks) > 0:
            count+=1
            cell = grid2d[nextBlanks[0][0]][nextBlanks[0][1]] #get the next cell from the blank cells queue
            if cell.val == 0:
                cell.findValidNums(grid2d)
            if len(cell.validNums) > 0:
                cell.setVal(cell.validNums.pop(0)) #try the first valid number for the cell, remove this number from its possible valid numbers list
                editedCells.append(nextBlanks.pop(0)) #remove the cell from nextBlanks as it has been edited and push it to the editedCells stack
            else: #if the cell has no valid numbers left then start backtracking
                cell.setVal(0) #set the current cell back to blank
                nextBlanks = [editedCells.pop()] #pop the last edited cell from the edited stack

        else: #if the nextBlanks queue is empty then add more blank cells to solve/end the algorithm
            nextBlanks = findNextBlanks(grid2d)
            if percentComplete(grid) == 100:
                run = False

    solution = []

    for i in range(81):
        solution.append(grid[i].val) #convert grid of objects to list of just values

    return solution
