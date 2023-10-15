class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}  # mapping of value and index
        for currentindex , value  in enumerate(nums):
            key = target-value
            if(key) in dictionary:
                return [dictionary[key] , currentindex]
            dictionary[value] = currentindex;    

