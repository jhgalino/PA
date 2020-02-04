inputList = []
while True:
    x = input()
    if x == "END":
        break
    else:
        inputList.append(x)

goldIndex = inputList.index("GOLD")
silverIndex = inputList.index("SILVER")
bronzeIndex = inputList.index("BRONZE")

gold = set(inputList[goldIndex + 1 : silverIndex])
silver = set(inputList[silverIndex + 1 : bronzeIndex])
bronze = set(inputList[bronzeIndex + 1 :])

meh1 = gold.intersection(silver)
meh2 = silver.intersection(bronze)
meh3 = bronze.intersection(gold)

meh4 = meh1.union(meh2, meh3)
meh5 = meh1.intersection(meh2, meh3)
meh6 = meh4.difference(meh5)

if len(meh6) != 0:
    for i in sorted(meh6):
        print(i)
else:
    print("NO RESULTS.")
