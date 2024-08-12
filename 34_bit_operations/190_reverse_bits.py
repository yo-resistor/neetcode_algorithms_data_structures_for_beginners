class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31
        while n:
            ans += (2 ** power) * (n % 2)
            n = n >> 1
            power -= 1
        
        return ans

def main():
    sol = Solution()
    
    print(sol.reverseBits(43261596))
    print(sol.reverseBits(4294967293))
    
if __name__ == "__main__":
    main()