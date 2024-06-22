class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        low = 1
        high = max(piles)
        
        while low < high:
            mid = (low + high) // 2
            if self.isFastEnough(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        
        return (low + high) // 2
    
    def isFastEnough(self, piles: list[int], k: int, h: int) -> bool:
        eating_hour = 0
        
        for pile in piles:
            # use ceiling of (pile / k) and add up to eating hour
            eating_hour += int(-(-(pile / k) // 1))
            
        return (eating_hour <= h)
        
        
def main():
    sol = Solution()
    
    piles = [1, 4, 3, 2]
    h = 9
    print(sol.minEatingSpeed(piles, h))
    
    piles = [25, 10, 23, 4]
    h = 4
    print(sol.minEatingSpeed(piles, h))
    
    piles = [30,11,23,4,20]
    h = 6
    print(sol.minEatingSpeed(piles, h))
    
if __name__ == "__main__":
    main()