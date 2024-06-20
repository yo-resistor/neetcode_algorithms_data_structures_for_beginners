def main():
    pairs = [(3, "a"), (9, "b"), (7, "c"), (6, "d"), (4, "e"), (10, "f"), (5, "g"), (1, "h"), (8, "i"), (2, "j"), (11, "k")]
    print(insertionSort(pairs))
    
def insertionSort(pairs):
    status = []
    for i in range(len(pairs)):
        j = i - 1
        while j >= 0 and pairs[j + 1][0] < pairs[j][0]:
            temp = pairs[j + 1]
            pairs[j + 1] = pairs[j]
            pairs[j] = temp
            j -= 1
        status.append(pairs[:])
    return status
    
main()
