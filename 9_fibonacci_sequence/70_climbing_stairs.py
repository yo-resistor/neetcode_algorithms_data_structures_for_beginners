class Solution:
    def climbStairs(self, n: int) -> int:
        # base case: no step
        if n <= 0:
            return 0
        
        # base case: step 1
        if n == 1:
            return 1
        
        # base case" step 2
        if n == 2:
            return 2
        
        # recursive case:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        
sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
