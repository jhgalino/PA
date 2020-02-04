# searches for occurrences of the first letter of a word in the grid
def searcher(value: str, i: int, matrix: list):
    positions = []
    for x, y in enumerate(matrix):
        if y == value:
            positions.append([i, x])
    return positions


# appends the searches in a list and returns it
def findFirstLetter(character: str, matrix: list):
    positionMatrix = []
    for i, v in enumerate(matrix):
        positionMatrix += searcher(character, i, v)
    return positionMatrix


# gets the direction of the word based on the location of the next letter
def directionGetter(char: str, location: list, grid: list):
    row, column = int(location[0]), int(location[1])
    direction = []
    possibleDirections = {}
    try:
        possibleDirections["north"] = grid[row - 1][column]
    except IndexError:
        pass

    try:
        possibleDirections["northwest"] = grid[row - 1][column - 1]
    except IndexError:
        pass

    try:
        possibleDirections["northeast"] = grid[row - 1][column + 1]
    except IndexError:
        pass

    try:
        possibleDirections["south"] = grid[row + 1][column]
    except IndexError:
        pass

    try:
        possibleDirections["southwest"] = grid[row + 1][column - 1]
    except IndexError:
        pass

    try:
        possibleDirections["southeast"] = grid[row + 1][column + 1]
    except IndexError:
        pass

    try:
        possibleDirections["east"] = grid[row][column + 1]
    except IndexError:
        pass
    try:
        possibleDirections["west"] = grid[row][column - 1]
    except IndexError:
        pass

    for i, v in possibleDirections.items():
        if v == char:
            direction.append(i)

    return direction


# look for match in surrounding lines of first letter
def get_string(direction: list, word: str, firstLetter: list, grid: list):
    actualLoc = ""
    for i in direction:
        outputString = grid[int(firstLetter[0])][int(firstLetter[1])]
        if i == "north":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row -= 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "south":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row += 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "west":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    column -= 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "east":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    column += 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "northwest":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row -= 1
                    column -= 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "northeast":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row -= 1
                    column += 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "southeast":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row += 1
                    column += 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        elif i == "southwest":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while True:
                try:
                    row += 1
                    column -= 1
                    outputString += grid[row][column]
                except IndexError:
                    break
        if word in outputString:
            actualLoc = "{} {}".format(firstLetter[0] + 1, firstLetter[1] + 1)
    return actualLoc


grid, wordsList = [], []
R, C = [int(x) for x in input().split()]
for i in range(R):
    grid.append(list(input()))
N = int(input())
for i in range(N):
    wordsList.append(input())

for i in wordsList:
    matchList = findFirstLetter(i[0], grid)
    location = ""
    for j in matchList:
        direction = directionGetter(i[1], j, grid)
        if len(direction) > 0:
            location = get_string(direction, i, j, grid)
        if len(location) > 1:
            print(location)
            break
