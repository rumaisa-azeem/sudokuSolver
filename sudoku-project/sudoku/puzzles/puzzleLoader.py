def puzzleLoader(): #loads 50 puzzles from text file, returns lists of puzzles by difficulty
    try:
        with open('puzzles.txt') as file:
            lines = file.read()
    except:
        with open('sudoku/puzzles/puzzles.txt') as file:
            lines = file.read()
        
    lines = lines.split('\n')
    puzzles = []

    for i in range(1,len(lines),10): #convert from raw text to list for each grid
        puzzle = []
        for j in range(i,i+9):
            for k in (list(lines[j])):
                puzzle.append(int(k))
                
        puzzles.append(puzzle)

    #split puzzles by difficulty
    easyPuzzles = []
    mediumPuzzles = []
    hardPuzzles = []
    for puzzle in puzzles:
        if puzzle.count(0) < 50:
            easyPuzzles.append(puzzle)
        elif puzzle.count(0) < 55:
            mediumPuzzles.append(puzzle)
        else:
            hardPuzzles.append(puzzle)

    return easyPuzzles, mediumPuzzles, hardPuzzles


easyPuzzles, mediumPuzzles, hardPuzzles = puzzleLoader()
