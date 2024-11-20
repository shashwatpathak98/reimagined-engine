class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We are provided an array
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:

            middle_index = (lower_bound + upper_bound) // 2

            if target == nums[middle_index]:
                return middle_index
            elif target > nums[middle_index]:
                lower_bound = middle_index + 1
            elif target < nums[middle_index]:
                upper_bound = middle_index - 1
        return -1
