from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0:
            queue = deque()
            visit = set()
            queue.append((0, 0))
            visit.add((0, 0))
            length = 1
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    # reach the destination
                    if r == n - 1 and c == n - 1:
                        return length
                    
                    neighbors = [[1, 0], [1, -1], [1, 1], [0, 1],
                                [-1, 0], [-1, -1], [-1, 1], [0, -1]]
                    for dr, dc in neighbors:
                        new_r, new_c = r + dr, c + dc
                        if (
                            min(new_r, new_c) < 0 or
                            max(new_r, new_c) == n or
                            grid[new_r][new_c] == 1 or
                            (new_r, new_c) in visit
                        ):
                            continue
                        queue.append((new_r, new_c))
                        visit.add((new_r, new_c))
                        
                length += 1
            
        return -1
        
        
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