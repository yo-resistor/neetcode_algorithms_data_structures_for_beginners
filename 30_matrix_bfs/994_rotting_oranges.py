from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # check if there is any fresh oranges or not
        if self.isFreshOrange(grid) == False:
            return 0
        
        # swap to add rotten orange (2) location in hash map
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visit.add((i, j))
        
        # check neighbor if they are fresh orange (1) turn into rotten orange (2) and register to the hash map
        # check neighbor if there are no oranges (0), do nothing
        # do this until the queue is empty
        elapsed = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in neighbors:
                    new_r, new_c = r + dr, c + dc
                    if (
                        min(new_r, new_c) < 0 or
                        new_r >= ROWS or new_c >= COLS or
                        (new_r, new_c) in visit or
                        grid[new_r][new_c] == 0
                    ):
                        continue
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))
        
            elapsed += 1
            
        # check if there is still any fresh oranges or not
        # if so, return -1
        # if not, return elapsed time
        if self.isFreshOrange(grid) == True:
            return -1
        
        return elapsed
    
    def isFreshOrange(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            if 1 in grid[i]:
                return True
        return False

def main():
    sol = Solution()
    
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(grid))
    
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(sol.orangesRotting(grid))
    
    grid = [[0,2]]
    print(sol.orangesRotting(grid))
    
if __name__ == "__main__":
    main()