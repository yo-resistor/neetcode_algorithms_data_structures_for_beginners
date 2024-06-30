class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # corner case: if there is nothing in nums
        if nums is None:
            return None
        
        results = []
        subset = []
        index = 0
        
        def dfs(index):
            # base case:
            if index >= len(nums):
                results.append(subset.copy())
                return
            
            # append the element
            subset.append(nums[index])
            dfs(index + 1)
            
            # Do not append the element
            subset.pop()
            dfs(index + 1)
            
        dfs(index)
            
        return results
    
def main():
    sol = Solution()
    
    nums = [1, 2, 3]
    print(sol.subsets(nums))
    
    nums = [0]
    print(sol.subsets(nums))
    
if __name__ == "__main__":
    main()