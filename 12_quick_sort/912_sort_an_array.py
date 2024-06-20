class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, arr: list[int], start: int, end: int) -> None:
        # base case
        if (end - start + 1) <= 1:
            return
        
        # recursive case
        left = start
        pivot = arr[end]
        
        # partition
        for i in range(start, end):
            if arr[i] <= pivot:
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1
        
        # move pivot
        arr[end] = arr[left]
        arr[left] = pivot
        
        # recursion
        self.quickSort(arr, start, left - 1)
        self.quickSort(arr, left + 1, end)
        
        return

def main():
    arr1 = [5, 2, 3, 1]
    arr2 = [5, 1, 1, 2, 0, 0]
    
    sol = Solution()
    print(sol.sortArray(arr1))
    print(sol.sortArray(arr2))
    
if __name__ == "__main__":
    main()