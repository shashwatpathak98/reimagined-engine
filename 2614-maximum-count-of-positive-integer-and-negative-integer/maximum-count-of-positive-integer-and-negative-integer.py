class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Linear Search

        # neg_count = 0
        # pos_count = 0
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         pos_count += 1
        #     elif nums[i] < 0:
        #         neg_count += 1
        # return max(neg_count , pos_count)

        # Binary Search
        lower_bound = 0
        upper_bound = len(nums) - 1

        pos_index = bisect_left(nums, 1)
        zero_index = bisect_left(nums, 0)

        pos_count = len(nums) - pos_index
        neg_count = zero_index
        return max(pos_count, neg_count)
