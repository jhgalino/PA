editHistory = []
userString = ""


def append(inp: str, userString: str):
    return userString + inp


def insert(index: int, inp: str, userString: str):
    string = list(userString)
    string.insert(index, inp)
    return "".join(string)


def undo(hist: list, userString: str):
    undoAction = hist.pop()
    if undoAction[0] == "append":
        userString = userString[::-1].replace(undoAction[1], "")
        userString = userString[::-1]
    elif undoAction[0] == "insert":
        userString = userString[: undoAction[1]] + userString[len(undoAction[2]) :]
    return userString


def save(hist: list, userString: str):
    global editHistory
    editHistory.clear()
    print(userString)
    return 0


while True:
    command = input()
    commandList = [x for x in command.split()]
    if commandList[0] == "append":
        editHistory.append(commandList)
        userString = append(commandList[1], userString)
    elif commandList[0] == "insert":
        editHistory.append(commandList)
        userString = insert(int(commandList[1]), commandList[2], userString)
    elif commandList[0] == "undo":
        if len(editHistory) > 0:
            userString = undo(editHistory, userString)
    elif commandList[0] == "save":
        save(editHistory, userString)
    elif commandList[0] == "exit":
        break

