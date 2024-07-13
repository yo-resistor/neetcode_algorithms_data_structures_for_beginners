class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            visit.add((r, c))
            return 1 + dfs(r, c + 1) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r - 1, c)
        
        area = 0    
        for i in range(ROWS):
            for j in range(COLS):
                area = max(area, dfs(i, j))
        
        return area


def main():
    sol = Solution()
    
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))
    
    grid = [[0,0,0,0,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))
    
if __name__ == "__main__":
    main()