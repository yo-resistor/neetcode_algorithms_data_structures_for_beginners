class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = self.countOnes(i)
        return ans
    
    def countOnes(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
        
def main():
    sol = Solution()
    
    print(sol.countBits(2))
    print(sol.countBits(5))
    
if __name__ == "__main__":
    main()