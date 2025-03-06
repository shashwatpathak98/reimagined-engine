class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                grid[i][j] = grid[i - 1][j - 1] + grid[i - 1][j]
        return grid
