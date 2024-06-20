arr = [1, 2, 3, 1]

n = len(arr)
for i in range(n):
    arr.append(arr[i])
    
print(arr)