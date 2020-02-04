numInputs = int(input())
inputList = []


def search(stringSearched: str, sentence: str):
    if sentence.find(stringSearched) != -1:
        return True
    else:
        return False


def replacer(
    sentence: str, replacement: str, toReplace: str,
):
    return sentence.replace(toReplace, replacement)


for i in range(2 * numInputs):
    inputList.append(input())
sentence = input()

for i in range(0, len(inputList), 2):
    while search(inputList[i], sentence):
        sentence = replacer(sentence, inputList[i + 1], inputList[i])

print(sentence)
