from collections import deque

class Solution():
    def shortestPath(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, 0))
        visit = set()
        visit.add((0, 0))
        
        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] == 1 or
                        (r + dr, c + dc) in visit
                    ):
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
            
def main():
    sol = Solution()
    
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    
    print(sol.shortestPath(grid))
    
if __name__ == "__main__":
    main()