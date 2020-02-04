inpList = sorted([int(x) for x in input().split()])
testCases = int(input())
sums = []
results = set([])

for i in range(testCases):
    sums.append(int(input()))


def removeItem(listToSearchIn: list, indexToRemove: int):
    return listToSearchIn[:indexToRemove] + listToSearchIn[indexToRemove + 1 :]


def checkForAddends(listToSearchIn: list, initialVal: int, total: int):
    result = list(set(list(filter(lambda x: x + initialVal == total, listToSearchIn))))
    return result[0]


# def searchForAddend(listToSearchIn: list, initialVal: int, totalToSearch: int):
#     for i, v in enumerate(listToSearchIn):
#         if initialVal + v == totalToSearch:
#             editedList = removeItem(listToSearchIn, i)
#             return v, editedList


# def iterateThroughList(listToSearchIn: list, totalToSearch: int):
#     for i in listToSearchIn:

for i in sums:
    for j in inpList:
        results.append(sorted((j, checkForAddends(inpList, j, i))))
    print(len(results))
    for k in results:
        print(" ".join(k))
