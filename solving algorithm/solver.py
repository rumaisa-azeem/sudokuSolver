import numpy as np
from cellClass import Cell
from sets import *
#from generator import generateRandomGrid
# this version has the solving algorithm as a module, can be used to generate grid

def printGrid(grid2d):
    if len(grid2d) != 9: #converts to 9x9 list if needed
        grid2d = to2d(grid2d).tolist()
    if type(grid2d[0][0]) == int:#if list grid is passed in
        for row in range(len(grid2d)):
            print(grid2d[row][0],grid2d[row][1],grid2d[row][2],'|',grid2d[row][3],grid2d[row][4],grid2d[row][5],'|',grid2d[row][6],grid2d[row][7],grid2d[row][8])
            if row == 2 or row == 5:
                print('---------------------')
    else: #if object grid is passed in
        for row in range (len(grid2d)):
            print(grid2d[row][0].val,grid2d[row][1].val,grid2d[row][2].val,'|',grid2d[row][3].val,grid2d[row][4].val,grid2d[row][5].val,'|',grid2d[row][6].val,grid2d[row][7].val,grid2d[row][8].val)
            if row == 2 or row == 5:
                print('---------------------')

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
    #print(">> grid is "+str(num)+"% complete")
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
    #print(percentComplete(grid))

    singleValidNumFound = True
    j = 1
    
    #find valid numbers for each cell
    while singleValidNumFound:
        #print('\nLOOP',j)
        singleValidNumFound = False

        for i in range(81):
            grid[i].findValidNums(grid2d)
            if len(grid[i].validNums) == 1:
                singleValidNumFound = True
                #print('\n> at cell',i,grid[i].coOrds)
                grid[i].setVal(grid[i].validNums[0]) 
                #print('set val to',grid[i].val)
            grid[i].resetValidNums()

        #print('result:')
        #printGrid(grid2d)
        j+=1


    #print('\nno more single valid numbers')
    grid2 = []
    currentGridVals = []
    for i in range(81):
        currentGridVals.append(grid[i].val)
    grid2 = currentGridVals #i think this is a variable to store the state of the grid after running the preliminary solver, has no actual function in the algorithm

    nextBlanks = findNextBlanks(grid2d) #the queue of the next cells to look at and consider the solutions for

    editedCells = []
    run = True
    count = 0
    grids = []

    while run:
        if len(nextBlanks) > 0:
            count+=1
            cell = grid2d[nextBlanks[0][0]][nextBlanks[0][1]]
            '''
            if cell.val != 0:
                print('\n> BACKTRACKING',count)
            else:
                print('\n>',count)
            '''
            #print('currently editing:',nextBlanks[0])
            if cell.val == 0:
                cell.findValidNums(grid2d)
            if len(cell.validNums) > 0:
                #print('valid nums=',cell.validNums)
                cell.setVal(cell.validNums.pop(0))
                #print('set cell val to',cell.val)
                editedCells.append(nextBlanks.pop(0))
            else:
                cell.setVal(0)
                #print('no more valid numbers')
                #print('edited cells:',editedCells)
                nextBlanks = [editedCells.pop()]

            #these lines are for debugging purposes, not part of solution
            currentGridVals = []
            for i in range(81):
                currentGridVals.append(grid[i].val)
            grids.append(currentGridVals)
            #########################################

        else:
            #print('\nrefreshing queue')
            nextBlanks = findNextBlanks(grid2d)
            if percentComplete(grid) == 100:
                run = False

    solution = []

    for i in range(81):
        solution.append(grid[i].val) #convert grid of objects to list of just values

    return solution
