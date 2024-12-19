class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #Remove element solution
        
        l = 0
        r = len(nums)-1
         
        while l <= r:
            if nums[l] == val:
                nums[l] , nums[r] = nums[r] , nums[l]
                r-=1
            else:
                l+=1
        return l


