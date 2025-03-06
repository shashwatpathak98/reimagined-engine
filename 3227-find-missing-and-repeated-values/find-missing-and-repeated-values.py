class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hash_map = {}

        for row in grid:
            for i in row:
                if i not in hash_map:
                    hash_map[i] = 1
                else:
                    hash_map[i] += 1

        missing, repeated = -1, -1
        for i in range(1, n * n + 1):
            if i not in hash_map:
                missing = i
            elif hash_map[i] == 2:
                repeated = i

        return [repeated, missing]
