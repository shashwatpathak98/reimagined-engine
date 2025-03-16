class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)
        left , right = 0 , len(queries)

        if not self.can_form_zero_array(nums, queries, right):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if self.can_form_zero_array(nums, queries , mid):
                right = mid -1
            else:
                left = mid + 1    
        return left    



    def can_form_zero_array(self, nums: list[int] , queries:List[List[int]], k:int) -> bool:
        
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n+1)

        for q in range(k):
            start , end, value = queries[q]

            difference_array[start] += value
            difference_array[end+1] -= value

        for i in range(n):
            total_sum += difference_array[i]
            if total_sum < nums[i]:
                return False
        return True        







            

        


        