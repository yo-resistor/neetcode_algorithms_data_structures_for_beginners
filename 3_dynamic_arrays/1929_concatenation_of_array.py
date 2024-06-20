class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        
        for i in range(length):
            ans[i] = nums[i]
            ans[i + length] = nums[i]
            
        return ans
    
sol = Solution()

case_1 = [1, 2, 1]
case_2 = [1, 3, 2, 1]

print(sol.getConcatenation(case_1))
print(sol.getConcatenation(case_2))