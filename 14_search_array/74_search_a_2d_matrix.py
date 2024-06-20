class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # get the size of matrix
        ROWS = len(matrix)
        if ROWS >= 1:
            COLS = len(matrix[0])
        else:
            COLS = 0
            
        # find the row where the target can be
        top = 0
        bot = ROWS - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
            
        if not (top <= bot):
            return False
        
        # run binary search in that target row
        row = (top + bot) // 2
        left = 0
        right = COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
            
        return False
        
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
target2 = 13

matrix2 = [[1]]
target3 = 0

matrix3 = [[1], [3]]
target4 = 3

sol = Solution()
print(sol.searchMatrix(matrix1, target1))
print(sol.searchMatrix(matrix1, target2))
print(sol.searchMatrix(matrix2, target3))
print(sol.searchMatrix(matrix3, target4))