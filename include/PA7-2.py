def doOperation(a: int, b: int, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b


def checkNum(a: str):
    try:
        a = int(a)
        return a
    except Exception:
        try:
            a = float(a)
            return a
        except Exception:
            return False


stack = []
printStr = []
inp = input().split()

try:
    for i in inp:
        if checkNum(i) is not False:
            printStr.append(i)
            stack.append(checkNum(i))
            print(stack)
        else:
            b = stack.pop()
            a = stack.pop()
            d = printStr.pop()
            c = printStr.pop()
            stack.append(doOperation(a, b, i))
            printStr.append("({} {} {})".format(c, i, d))
            print(stack)
    if len(stack) == 1:
        print("{} = {}".format(printStr[0], stack[0]))
    else:
        print("Invalid expression.")
except Exception:
    print("Invalid expression.")

