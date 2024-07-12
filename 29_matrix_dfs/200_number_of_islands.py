class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        return 0
    
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