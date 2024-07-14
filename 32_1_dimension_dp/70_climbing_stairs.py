class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        ways = [1, 2]
        i = 3
        while i <= n:
            temp = ways[1]
            ways[1] += ways[0]
            ways[0] = temp
            i += 1
            
        return ways[1]
    
def main():
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(10))
    
if __name__ == "__main__":
    main()