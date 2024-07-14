class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        # make graph first with the given prerequisites
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        # run dfs for each course to check whether there is closed cycle or not
        # if there is closed cycle, False
        # if there is no closed cycle, True
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs] == []:
                return True
            
            visit.add(crs)
            for pre in graph[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            graph[crs] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
        
        
def main():
    sol = Solution()
    
    numCourses = 2
    prerequisites = [[1, 0]]
    print(sol.canFinish(numCourses, prerequisites))
    
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(sol.canFinish(numCourses, prerequisites))
    
    numCourses = 1
    prerequisites = []
    print(sol.canFinish(numCourses, prerequisites))
    
if __name__ == "__main__":
    main()