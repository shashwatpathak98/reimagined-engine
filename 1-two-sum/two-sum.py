class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]
        
        
        #Optimized approach
        

        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i , hashmap[complement]]
            else:
                hashmap[nums[i]] = i    



        