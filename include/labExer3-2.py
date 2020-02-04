queue = []
n = int(input())
while True:
    inp = input().split("-")
    if inp != r'#RUNNINGMANinManila':
        queue.append(inp)
    else:
        break

pattern = ["priority", "priority", "gold", "regular", "gold"]

for i in pattern:
    
