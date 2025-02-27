class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            ans += [nums[j] for j in range(len(nums))]
        return ans    

        