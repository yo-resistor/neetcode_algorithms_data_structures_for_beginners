class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2
    
def main():
    sol = Solution()
    print(sol.rob(nums=[1,2,3,1]))
    print(sol.rob(nums=[2,7,9,3,1]))
    
if __name__ == "__main__":
    main()