class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
       rs = []
       for i in range(n):
        rs.append(nums[i])
        rs.append(nums[i+n])
       return rs                


        