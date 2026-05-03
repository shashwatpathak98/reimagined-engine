class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1 , n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # Two Pointers
        nums_with_index = sorted([[num, i] for i, num in enumerate(nums)])
        n = len(nums_with_index) - 1
        l,r = 0,n
        while l<r:
            sum = nums_with_index[l][0] + nums_with_index[r][0]
            if sum == target:
                return [nums_with_index[l][1],nums_with_index[r][1]]
            elif sum < target:
                l+=1
            else:
                r-=1
        return []        
                      




        