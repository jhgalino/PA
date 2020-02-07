testCases = int(input())
z = []
inps = []
k = []
for i in range(testCases):
    z.append(int(input()))
    inps.append([int(x) for x in input().split()])
    k.append(int(input()))


def adder(l: list, n: int):
    l = l[::-1]
    total = 0
    for i in l[:n]:
        total += i
    return total


def zbonnaci(inp: list, k: int, z: int):
    length = len(inp) - 1
    if length < k:
        inp.append(adder(inp, z))
        return zbonnaci(inp, k, z)
    else:
        return inp

for i in range(len(z)):
    ans = zbonnaci(inps[i], k[i], z[i])
    print(int(ans[k[i]]) + z[i])
