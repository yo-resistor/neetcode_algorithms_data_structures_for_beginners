class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # solution 1
        # length = len(nums)
        # idx = 0
        
        # if length != 0:
        #     for i in range(length):
        #         if i == 0:
        #             idx += 1
        #         elif nums[i] != nums[i - 1]:
        #             nums[idx] = nums[i]
        #             idx += 1

        # return idx
        
        # solution 2: better
        idx = 0 
        length = len(nums)
        
        if length != 0:
            idx += 1
            
            for i in range(length):
                if nums[idx - 1] != nums[i]:
                    nums[idx] = nums[i]
                    idx += 1
                    
        return idx

case_1 = [1, 1, 2]
case_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
case_3 = []
case_4 = [1]
case_5 = [1, 1]

sol = Solution()

print(sol.removeDuplicates(case_1))
print(sol.removeDuplicates(case_2))
print(sol.removeDuplicates(case_3))
print(sol.removeDuplicates(case_4))
print(sol.removeDuplicates(case_5))