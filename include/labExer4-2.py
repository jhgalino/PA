inputs = []
testCases = int(input())
for i in range(testCases):
    inputs.append(list(input()))


def check(a: str):
    global curlsOpen, curlsClose, bracksClose, bracksOpen, parensClose, parensOpen
    if a == "{":
        curlsOpen += 1
    elif a == "}":
        curlsClose += 1
    elif a == "[":
        bracksOpen += 1
    elif a == "]":
        bracksClose += 1
    elif a == "(":
        parensOpen += 1
    elif a == ")":
        parensClose += 1
    return


def traverse(eyyy: list):
    if len(eyyy) > 1:
        a = eyyy[0]
        check(a)
        eyyy = eyyy[1:]
        traverse(eyyy)
    else:
        a = eyyy[0]
        check(a)

    return


for i in inputs:
    curlsOpen, curlsClose = 0, 0
    bracksOpen, bracksClose = 0, 0
    parensOpen, parensClose = 0, 0
    traverse(i)
    if (
        curlsOpen == curlsClose
        and bracksOpen == bracksClose
        and parensOpen == parensClose
    ):
        print("True")
    else:
        print("False")
