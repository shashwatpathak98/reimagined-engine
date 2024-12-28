class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = []
        a = nums
        index = 1
        a[0] = nums[0]
   
        for numb in range(1,len(a)):
            if a[index-1] != nums[numb]:
                a[index] = nums[numb]
                index=index+1
        return index        


        