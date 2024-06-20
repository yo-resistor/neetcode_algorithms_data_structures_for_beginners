class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counts = [0, 0, 0]
        
        for i in nums:
            counts[i] += 1
        
        index = 0
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[index] = j
                index += 1
        
nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 1]
        
sol = Solution()
sol.sortColors(nums1)
print(nums1)
sol.sortColors(nums2)
print(nums2)