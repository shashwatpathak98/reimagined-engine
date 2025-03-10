class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        hash_map = {}

        for rows in grid:
            for num in rows:
                hash_map[num] = hash_map.get(num , 0) + 1

        missing , repeated = -inf, -inf
        for i in range(1, n * n + 1):
            if i not in hash_map:
                missing = i
            elif hash_map[i] == 2:
                repeated = i
        return [repeated , missing]        




        