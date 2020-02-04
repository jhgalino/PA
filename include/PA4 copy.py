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
def directionGetter(char: str, location: list, grid: list, rows: int, cols: int):
    row, column = int(location[0]), int(location[1])
    direction = []
    possibleDirections = {}
    if row - 1 >= 0:
        possibleDirections["north"] = grid[row - 1][column]
    if row - 1 >= 0 and column - 1 >= 0:
        possibleDirections["northwest"] = grid[row - 1][column - 1]
    if row - 1 >= 0 and column + 1 <= cols:
        possibleDirections["northeast"] = grid[row - 1][column + 1]
    if row + 1 <= rows:
        possibleDirections["south"] = grid[row + 1][column]
    if row + 1 <= rows and column - 1 >= 0:
        possibleDirections["southwest"] = grid[row + 1][column - 1]
    if row + 1 <= rows and column + 1 <= cols:
        possibleDirections["southeast"] = grid[row + 1][column + 1]
    if column + 1 <= cols:
        possibleDirections["east"] = grid[row][column + 1]
    if column - 1 >= 0:
        possibleDirections["west"] = grid[row][column - 1]

    for i, v in possibleDirections.items():
        if v == char:
            direction.append(i)

    return direction


# look for match in surrounding lines of first letter
def get_string(
    direction: list, word: str, firstLetter: list, grid: list, r: int, c: int
):
    actualLoc = ""
    for i in direction:
        outputString = grid[int(firstLetter[0])][int(firstLetter[1])]
        if i == "north":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row >= 0:
                row -= 1
                outputString += grid[row][column]
        elif i == "south":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row < r:
                row += 1
                outputString += grid[row][column]
        elif i == "west":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while column > 0:
                column -= 1
                outputString += grid[row][column]
        elif i == "east":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while column < c:
                column += 1
                outputString += grid[row][column]
        elif i == "northwest":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row > 0 and column > 0:
                row -= 1
                column -= 1
                outputString += grid[row][column]
        elif i == "northeast":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row > 0 and column < c:
                row -= 1
                column += 1
                outputString += grid[row][column]
        elif i == "southeast":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row < r and column < c:
                row += 1
                column += 1
                outputString += grid[row][column]
        elif i == "southwest":
            row = int(firstLetter[0])
            column = int(firstLetter[1])
            while row < r and column > 0:
                row += 1
                column -= 1
                outputString += grid[row][column]
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
    location = "{} {}".format(matchList[0][0] + 1, matchList[0][1] + 1)
    a = ""
    direction = []
    for j in matchList:
        if len(i) > 1:
            direction = directionGetter(i[1], j, grid, R - 1, C - 1)
        if len(direction) > 0:
            a = get_string(direction, i, j, grid, R - 1, C - 1)
        if len(a) > 1:
            location = a
            break
    print(location)
