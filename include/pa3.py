testcases = int(input())
matrix = []
for i in range(testcases):
    matrix.append(int(input()))


def swap(a: int, b: int, z: list):
    get = z[a], z[b]
    z[b], z[a] = get
    return z


def printer(z: list, index: int):
    for i, v in enumerate(z):
        if i == index:
            print("[{}]".format(z[i]), end=" ")
        else:
            print(v, end=" ")
    print("")


def left_to_right(z: list):
    start = 0
    sorted = True
    for i, v in enumerate(z):
        if v >= z[start] and i != 0:
            start = start + 1
            printer(z, start)
        elif v < z[start]:
            z = swap(start, start+1, z)
            start = start + 1
            sorted = False
            printer(z, start)
    if sorted is True:
        return 0
    else:
        right_to_left(z)


def right_to_left(z: list):
    start = len(z) - 1
    sorted = True
    for i, v in enumerate(z[::-1]):
        if v > z[start]:
            z = swap(start - 1, start, z)
            start = start - 1
            sorted = False
            printer(z, start)
        elif v <= z[start] and i != 0:
            start = start - 1
            printer(z, start)
    if sorted is True:
        return 0
    else:
        left_to_right(z)


printer(matrix, len(matrix)-1)
right_to_left(matrix)

