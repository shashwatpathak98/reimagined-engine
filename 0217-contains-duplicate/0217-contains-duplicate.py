class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            key = nums[i]
            defaultValue = 1
            if key in hashmap: 
                return True            
            hashmap[nums[i]] = defaultValue
        return False
               
               
                
            