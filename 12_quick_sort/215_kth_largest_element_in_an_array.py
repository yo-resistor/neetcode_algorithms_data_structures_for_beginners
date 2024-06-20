class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        k = len(nums) - k
        
        p = self.partition(nums, left, right)
        
        while p != k:
            if p > k:
                p = self.partition(nums, left, p - 1)
            else: 
                p = self.partition(nums, p + 1, right)
            
        return nums[p] 
    
    def partition(self, nums: list[int], start: int, end: int) -> int:
        pointer = start
        pivot = nums[end]
        
        for i in range(start, end):
            # if the value is less than or equal to the pivot, fill and move the pointer
            # else fill but do not move the pointer
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
            
        nums[end] = nums[pointer]
        nums[pointer] = pivot
        
        return pointer
    
def main():
    nums1 = [3, 2, 1, 5, 6, 4]
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    
    sol = Solution()
    print(sol.findKthLargest(nums1, 2))
    print(sol.findKthLargest(nums2, 4))
    
if __name__ == "__main__":
    main()