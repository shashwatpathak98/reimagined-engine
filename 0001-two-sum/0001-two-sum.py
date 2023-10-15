class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}  # mapping of value and index
        for currentindex , value  in enumerate(nums):
            if(target - value) in dictionary:
                return [dictionary[target-value] , currentindex]
            dictionary[value] = currentindex;    

