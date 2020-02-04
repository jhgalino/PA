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


def zigzagzort(Z: list):
    start = len(Z) - 1
    end = 0
    swapped = True
    while True:
        swapped = False
        for i in range(start, end - 1, -1):
            if i == start:
                printer(Z, i)
            else:
                if Z[i + 1] < Z[i]:
                    Z = swap(i, i + 1, Z)
                    swapped = True
                printer(Z, i)

        if swapped is False:
            break

        swapped = False
        end = end + 1
        tempStart = start
        start = end
        end = tempStart

        for i in range(start, end + 1):
            if i == start:
                printer(Z, i)
            else:
                if Z[i] < Z[i - 1]:
                    Z = swap(i, i - 1, Z)
                    swapped = True
                printer(Z, i)

        end = end - 1
        tempStart = start
        start = end
        end = tempStart

    return Z


testcases = int(input())
matrix = []
for i in range(testcases):
    matrix.append(int(input()))

zigzagzort(matrix)
