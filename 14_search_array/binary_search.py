class Solution():
    def search(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            M = (L + R) // 2
            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M
        
        return -1
        
nums1 = [-1,0,2,4,6,8] 
target1 = 4

nums2 = [-1,0,2,4,6,8]
target2 = 3

sol = Solution()
print(sol.search(nums1, target1))
print(sol.search(nums2, target2))