editHistory = []
string = ""


def goThroughHistory(hist: list, inp: str):
    st = inp
    for i in hist:
        if i[0] == "append":
            st += str(i[1])
        elif i[0] == "insert":
            st = list(st)
            st.insert(int(i[1]), i[2])
            st = "".join(st)
    return st


while True:
    command = input()
    if command == "exit":
        break
    elif command == "save":
        meh = goThroughHistory(editHistory, string)
        print(meh)
    elif command == "undo":
        if len(editHistory) > 0:
            editHistory.pop()
    else:
        editHistory.append(command.split())
