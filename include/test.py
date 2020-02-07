def traverser(l: list):
    if len(l) > 1:
        print(l[0])
        l = l[1:]
        traverser(l)
    else:
        print(l[0])
        return 

print(traverser([1,2,3,4,5]))