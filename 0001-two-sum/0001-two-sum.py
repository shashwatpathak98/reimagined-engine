class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}  # mapping of value and index
        for currentindex , currentelement  in enumerate(nums):
            compliment = target - currentelement
            if(compliment) in dictionary:
                return [dictionary[compliment] , currentindex]
            dictionary[currentelement] = currentindex;    

