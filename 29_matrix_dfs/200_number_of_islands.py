class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == "0" or
                (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            
            neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
            
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    islands += 1
                    dfs(i, j)
        
        return islands
    
def main():
    sol = Solution()
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    print(sol.numIslands(grid))
    
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid))
    
if __name__ == "__main__":
    main()