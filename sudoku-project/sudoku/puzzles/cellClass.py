from sudoku.puzzles.sets import *

# class to store each cell as an object in the grid
class Cell:

    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.coOrds = [self.row, self.col]
        self.val = val
        if self.val == 0:
            self.canEdit = True
            self.isEdited = False
            self.validNums = []
        else:
            self.canEdit = False
            self.isEdited = False
            self.validNums = []

        for count in range(9):
            if self.coOrds in allSets[count]:
                self.set = allSets[count]

    def setVal(self, val):
        self.val = val
        if not self.isEdited:
            self.isEdited = True

    def findValidNums(self, grid):  # grid must be 2d 9x9

        if not self.canEdit:
            return

        invalidNums = []

        for i in range(9):
            #print('checking across row', i)
            checkingCell = grid[self.row][i].val
            if checkingCell != 0 and checkingCell not in invalidNums:
                invalidNums.append(checkingCell)

        for i in range(9):
            #print('checking down column', i)
            checkingCell = grid[i][self.col].val
            if checkingCell != 0 and checkingCell not in invalidNums:
                invalidNums.append(checkingCell)

        for i in range(9):
            #print('checking set', self.set[i])
            checkingCell = grid[self.set[i][0]][self.set[i][1]].val
            if checkingCell != 0 and checkingCell not in invalidNums:
                invalidNums.append(checkingCell)

        for i in range(1, 10):
            if i not in invalidNums:
                self.validNums.append(i)
        
        return self.validNums

    def resetValidNums(self):
        self.validNums = []
