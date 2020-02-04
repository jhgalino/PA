inpList = sorted([int(x) for x in input().split()])
testCases = int(input())
sums = []
results = set()

for i in range(testCases):
    sums.append(int(input()))


def removeItem(listToSearchIn: list, indexToRemove: int):
    return listToSearchIn[:indexToRemove] + listToSearchIn[indexToRemove + 1 :]


def checkForAddends(listToSearchIn: list, initialVal: int, total: int):
    result = list(set(list(filter(lambda x: x + initialVal == total, listToSearchIn))))
    if len(result) > 0:
        return result[0]


for i in sums:
    for j in inpList:
        results.add(tuple(sorted((j, checkForAddends(inpList, j, i)))))
    results = sorted(list(results))
    print(len(results))
    for k in results:
        print(" ".join(str(i) for i in k))
    results = set()
