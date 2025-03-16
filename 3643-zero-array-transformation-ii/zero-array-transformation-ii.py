class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        # length of nums array , start index and end index of queries array
        n, start, end = len(nums), 0, len(queries)

        # If zero array cannot be formed return -1
        if not self.can_form_zero_array(nums, queries, end):
            return -1

        # Binary search to find minimum range at which nums will be zero
        while start <= end:
            mid = (start + end) // 2
            if self.can_form_zero_array(nums, queries, mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

    # Helper Function to check if zero array can be formed
    def can_form_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        # Differnce array - to include range of elements
        difference_array = [0] * (n + 1)
        # prefix_sum represents the total value applied from the queries up to the current index i
        prefix_sum = 0

        # Fill difference array
        for i in range(k):

            # get start, end and values from queries
            start, end, val = queries[i]

            # Calculate the difference array
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if the prefix_sum of difference array is less than any of the nums element,
        # if yes that means it cannot form zero array, so return False
        for i in range(n):
            prefix_sum += difference_array[i]
            # if the prefix_sum is less than nums[i], it means the required value at that index can't be reached using the queries processed so far.
            # Hence,return False
            if prefix_sum < nums[i]:
                return False
        # all indices in nums can be satisfied, and it returns True.
        return True
