operations = ["5","-2","4","C","D","9","+","+"]

scores = []
for i in range(len(operations)):
    print(i)
    if operations[i] == "+":
        scores.append(scores[-1] + scores[-2])
    elif operations[i] == "D":
        scores.append(2 * scores[-1])
    elif operations[i] == "C":
        scores.pop()
    else:
        scores.append(int(operations[i]))
    print(scores)
        
print(sum(scores))