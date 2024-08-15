class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        prev_row = [0] * n
        prev_row[n - 1] = 1
        
        for r in reversed(range(m)):
            cur_row = [0] * n
            for c in reversed(range(n)):
                if obstacleGrid[r][c] == 1:
                    cur_row[c] = 0
                elif c + 1 == n:
                    cur_row[c] = prev_row[c]
                else:
                    cur_row[c] = cur_row[c + 1] + prev_row[c]
            prev_row = cur_row
        
        return prev_row[0]
        
        
def main():
    sol = Solution()
    
    obstacleGrid = [[0,1],[0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
    
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
    
if __name__ == "__main__":
    main()