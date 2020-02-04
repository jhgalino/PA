inpList = sorted([int(x) for x in input().split()])
testCases = int(input())
sums = []
results = set()

for i in range(testCases):
    sums.append(int(input()))


def removeItem(listToSearchIn: list, indexToRemove: int):
    return listToSearchIn[:indexToRemove] + listToSearchIn[indexToRemove + 1 :]


def checkForAddends(listToSearchIn: list, initialVal: int, total: int):
    result = set(list(filter(lambda x: x + initialVal == total, listToSearchIn)))
    result = list(result)
    if len(result) > 0:
        return result[0]
    else:
        return -1


for i in sums:
    for j, v in enumerate(inpList):
        tempList = removeItem(inpList, j)
        z = checkForAddends(tempList, inpList[j], i)
        if z != -1:
            results.add(tuple(sorted((inpList[j], z))))
    results = sorted(list(results))
    print(len(results))
    for k in results:
        print(" ".join(str(i) for i in k))
    results = set()
