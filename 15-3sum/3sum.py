class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        #Brute force approach
        # triplet_set = set()
        # sorted_nums = sorted(nums)
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
        #                 triplet = tuple(sorted([sorted_nums[i], sorted_nums[j], sorted_nums[k]]))
        #                 triplet_set.add(triplet)
        # return [list(triplet) for triplet in triplet_set]                
                        
        #Two pointer approach
        triplet_set = []
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)):
            
            target, sum_start = -sorted_nums[i], i+1
            if i>0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
             
            sum_pairs = self.find_pairs(sorted_nums, target, sum_start)

            for pair in sum_pairs:
                triplet_set.append([sorted_nums[i]] + pair)
        return triplet_set        


    def find_pairs(self, arr, target, start):
        l, r = start, len(arr)-1
        pairs = []

        while l < r:
            sums = arr[l] + arr[r]
            if  sums == target:
                pairs.append([arr[l],arr[r]])
                l+=1
                while l < r and arr[l-1] == arr[l]:
                    l+=1
            elif sums < target:
                l+=1
            else:
                r-=1
        return pairs                

        
        


                



