class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in nums:
            remain = target - num
            index1 = nums.index(num)
            if remain in nums[(index1 + 1):]:
                index2 = nums.index(remain, index1 + 1)
                return [index1, index2]
        return []
    
def main():
    sol = Solution()
    
    print(sol.twoSum(nums=[2,7,11,15], target=9))
    print(sol.twoSum(nums=[3,2,4], target=6))
    print(sol.twoSum(nums=[3,3], target=6))
    
if __name__ == "__main__":
    main()