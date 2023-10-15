class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in hashmap: 
                return True
            else:               
                hashmap[key] = 1
        return False
               
               
                
            