class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # corner case: if there is nothing in nums
        if nums is None:
            return None
        
        results = []
        subset = []
        
        def dfs(i):
            # base case:
            if i >= len(nums):
                results.append(subset.copy())
                return
            
            # append the element
            subset.append(nums[i])
            dfs(i + 1)
            
            # Do not append the element
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
            
        return results
    
def main():
    sol = Solution()
    
    nums = [1, 2, 3]
    print(sol.subsets(nums))
    
    nums = [0]
    print(sol.subsets(nums))
    
if __name__ == "__main__":
    main()