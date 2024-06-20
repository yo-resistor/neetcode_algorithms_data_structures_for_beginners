class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        idx = 0
        length = len(nums)
        
        if length != 0:
            for i in range(length):
                if nums[i] != val:
                    nums[idx] = nums[i]
                    idx += 1
        
        return idx
        
case_1 = [3, 2, 2, 3]
case_2 = [0, 1, 2, 2, 3, 0, 4, 2]
        
sol = Solution()

print(sol.removeElement(case_1, 2))
print(sol.removeElement(case_2, 2))