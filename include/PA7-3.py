inpList = input().split()
stack = []
printStack = []

def checkIfNum(a: int):
    try:
        int(a)
        return True
    except Exception:
        return False


for i in inpList:
    if checkIfNum(i):
        stack.append(int(i))
        printStack.append(i)
    else:
        b = stack.pop()
        a = stack.pop()
        d = printStack.pop()
        c = printStack.pop()
        if i == "+":
            stack.append(a + b)
        elif i == "-":
            stack.append(a - b)
        elif i == "*":
            stack.append(a * b)
        elif i == "/":
            stack.append(a//b)