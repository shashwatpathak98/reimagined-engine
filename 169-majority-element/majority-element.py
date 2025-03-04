class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_value = -inf
        max_key = -inf
        for k , v in counts.items():  
            if v > max_value:
                max_value = v
                max_key = k
        return max_key        


        