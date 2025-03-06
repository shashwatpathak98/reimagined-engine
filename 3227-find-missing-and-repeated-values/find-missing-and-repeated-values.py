class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hash_map = {}

        for row in grid:
            for i in row:
                hash_map[i] = hash_map.get(i , 0) + 1

        missing, repeated = -1, -1
        for i in range(1, n * n + 1):
            if i not in hash_map:
                missing = i
            elif hash_map[i] == 2:
                repeated = i

        return [repeated, missing]
