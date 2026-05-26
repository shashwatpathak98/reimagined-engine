class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force Approach
        # n = len(height)
        # max_water = 0

        # for i in range(n):
        #     for j in range(i+1, n):
        #         water = min(height[i], height[j]) * (j-i)
        #         max_water = max(max_water, water)
        # return max_water      

        #Two Pointers Approach
        left, right = 0, len(height) - 1
        max_water = 0 

        while left < right:

            water = min(height[left], height[right]) * (right-left)
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left+=1
            elif height[left] > height[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max_water        




        