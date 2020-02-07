inputs = []
testCases = int(input())
for i in range(testCases):
    inputs.append(list(input()))


def check(a: str):
    global totalSum
    if a == "{":
        totalSum += 1
    elif a == "}":
        totalSum -= 1
    elif a == "[":
        totalSum += 2
    elif a == "]":
        totalSum -= 2
    elif a == "(":
        totalSum += 3
    elif a == ")":
        totalSum -= 3
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
    totalSum = 0
    traverse(i)
    if totalSum == 0:
        print("True")
    else:
        print("False")
