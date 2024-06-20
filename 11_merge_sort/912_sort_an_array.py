class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2 + 1
        
        arr_left = self.sortArray(nums[start:mid])
        arr_right = self.sortArray(nums[mid:])
        
        return self.merge(arr_left, arr_right)
    
    def merge(self, arr_left: list[int], arr_right: list[int]) -> list[int]:
        merged = [None] * (len(arr_left) + len(arr_right))
        
        i, j, k = 0, 0, 0
        
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] <= arr_right[j]:
                merged[k] = arr_left[i]
                k += 1
                i += 1
            else:
                merged[k] = arr_right[j]
                k += 1
                j += 1
        
        while i < len(arr_left):
            merged[k] = arr_left[i]
            k += 1
            i += 1
            
        while j < len(arr_right):
            merged[k] = arr_right[j]
            k += 1
            j += 1
        
        return merged

def main():
    arr1 = [5, 2, 3, 1]
    arr2 = [5, 1, 1, 2, 0, 0]
    
    sol = Solution()
    print(sol.sortArray(arr1))
    print(sol.sortArray(arr2))
    
if __name__ == "__main__":
    main()