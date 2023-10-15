class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        value = 1
        for i in range(len(nums)):
            key = nums[i]
            if key in hashmap: 
                return True            
            hashmap[key] = value     
        return False
               
               
                
            