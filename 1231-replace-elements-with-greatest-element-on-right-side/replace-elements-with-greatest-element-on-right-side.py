class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse order iteration
        # new max = max( oldmax , arr[i])
        
        right_max = -1

        for i in range(len(arr)-1 , -1 , -1):
            new_max = max(right_max , arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr    



        