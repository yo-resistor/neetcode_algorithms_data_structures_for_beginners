class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        # helper function to count unique paths from start to end
        def dfs(grid, row, col, visit):
            ROWS, COLS = len(grid), len(grid[0])
            
            # base case 1: return 0
            if (
                min(row, col) < 0 or
                row == ROWS or col == COLS or
                (row, col) in visit or
                grid[row][col] == 1
            ):
                return 0
            
            # base case 2: return 1
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            # recursive case
            visit.add((row, col))
            
            count = 0
            count += dfs(grid=grid, row=row+1, col=col, visit=visit)
            count += dfs(grid=grid, row=row-1, col=col, visit=visit)
            count += dfs(grid=grid, row=row, col=col+1, visit=visit)
            count += dfs(grid=grid, row=row, col=col-1, visit=visit)
            
            visit.remove((row, col))
            
            return count
        
        return dfs(grid=grid, row=0, col=0, visit=set())
    
def main():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    
    sol = Solution()
    print(sol.countPaths(grid=grid))
    
if __name__ == "__main__":
    main()