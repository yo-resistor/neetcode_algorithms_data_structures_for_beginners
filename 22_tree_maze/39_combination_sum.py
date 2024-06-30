class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # corner case: impossible to get target out of candidates
        if min(candidates) > target:
            return []
            
        results = []
        
        def dfs(index, current, total):
            # if the total of current set is equal to target
            if total == target:
                results.append(current.copy())
                return
                
            # if index is out of bound or the total is bigger than target
            if index >= len(candidates) or total > target:
                return
            
            # recursive case: add indexed candidate to current set
            current.append(candidates[index])
            dfs(index, current, total + candidates[index])
            
            # recursive case: do not add indexed candidate to current set
            current.pop()
            dfs(index + 1, current, total)
            
        dfs(index=0, current=[], total=0)
        
        return results
    
def main():
    sol = Solution()
    
    candidates = [2,3,6,7] 
    target = 7
    print(sol.combinationSum(candidates, target))
    
    candidates = [2,3,5]
    target = 8
    print(sol.combinationSum(candidates, target))
    
    candidates = [2]
    target = 1
    print(sol.combinationSum(candidates, target))
    
if __name__ == "__main__":
    main()