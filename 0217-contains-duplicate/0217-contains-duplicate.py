class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {} 
        for i in range(len(nums)):
            if nums[i] in hashmap: 
                return True 
            elif nums[i] not in hashmap:           
                hashmap[nums[i]] = 1     
        return False
               
               
                
            