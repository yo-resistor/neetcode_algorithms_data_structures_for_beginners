class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        path_lengths = []
        
        def dfs(grid, r, c, path):
            # base case 1: out of bound, in the path, not viable
            if (
                min(r, c) < 0 or
                max(r, c) >= n or
                (r, c) in path or
                grid[r][c] == 1 
            ):
                return 0
            
            # base case 2: reach the goal
            if (r == n - 1 and c == n - 1):
                path.add((r, c))
                path_lengths.append(len(path))
                path.remove((r, c))
                return 1
            
            # recursive case
            path.add((r, c))
            
            count = 0
            count += dfs(grid, r, c + 1, path)
            count += dfs(grid, r + 1, c + 1, path)
            count += dfs(grid, r + 1, c, path)
            count += dfs(grid, r + 1, c - 1, path)
            count += dfs(grid, r, c - 1, path)
            count += dfs(grid, r - 1, c - 1, path)
            count += dfs(grid, r - 1, c, path)
            count += dfs(grid, r - 1, c + 1, path)
                        
            path.remove((r, c))
            
            return count
        
        if dfs(grid=grid, r=0, c=0, path=set()) == 0:
            return -1
        else:
            return min(path_lengths)
            
def main():
    sol = Solution()
    
    grid = [[0,1],[1,0]]
    print(sol.shortestPathBinaryMatrix(grid))
    
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(sol.shortestPathBinaryMatrix(grid))
    
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    print(sol.shortestPathBinaryMatrix(grid))
    
if __name__ == "__main__":
    main()