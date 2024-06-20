class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        
class Solution:
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
        
    def quickSortHelper(self, arr: list[Pair], start: int, end: int) -> None:
        # base case
        if (end - start + 1) <= 1:
            return
        
        # recursion: partition
        pivot = arr[end]
        left = start
        
        for i in range(start, end):
            if arr[i].key <= pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        
        # recursion: move pivot
        arr[end] = arr[left]
        arr[left] = pivot
        
        # recursion
        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)
        
        # return the sorted result
        return arr
    
    def printPairs(self, pairs: list[Pair]) -> None:
        arr = []
        for i in range(len(pairs)):
            arr.append((pairs[i].key, pairs[i].value))
        
        print(arr)
    
def main():
    pairs1 = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
    pairs2 = [Pair(5, "apple"), Pair(9, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")]
    
    sol = Solution()
    sol.quickSort(pairs1)
    sol.printPairs(pairs1)
    sol.quickSort(pairs2)
    sol.printPairs(pairs2)
    
if __name__ == "__main__":
    main()