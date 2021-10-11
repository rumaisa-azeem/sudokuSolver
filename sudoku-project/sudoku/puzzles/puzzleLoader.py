try:
    with open('puzzles.txt') as file:
        lines = file.read()
except:
    with open('sudoku/puzzles/puzzles.txt') as file:
        lines = file.read()
    

print(lines)
puzzleList = lines.split('\n')
print(puzzleList
)