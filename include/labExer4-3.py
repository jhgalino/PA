def F(num: list):
    a = add(num)
    if len(a) == 1:
        return a[0]
    else:
        return F(a)


def add(add: list):
    x = 0
    for i in add:
        x += int(i)
    return list(str(x))


times = int(input())

for i in range(times):
    n = list(input())
    print(F(n))

