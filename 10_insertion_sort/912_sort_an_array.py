class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                j -= 1
            
        return nums
        
def main():
    nums = [5, 2, 3, 1]
    
    sol = Solution()
    print(sol.sortArray(nums))
    
if __name__ == "__main__":
    main()
