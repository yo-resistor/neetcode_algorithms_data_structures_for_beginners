class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = set()
        for num in nums:
            if num not in hashmap:
                hashmap.add(num)
            else:
                return True
        return False
    
def main():
    sol = Solution()
    
    print(sol.containsDuplicate(nums=[1,2,3,1]))
    print(sol.containsDuplicate(nums=[1,2,3,4]))
    print(sol.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))
    
if __name__ == "__main__":
    main()