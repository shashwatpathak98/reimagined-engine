class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #  return str(x) == str(x)[::-1]
        # Optimized Approach
        numsArray = str(x)
        start = 0
        end = len(numsArray) - 1
        while start < end:
            if numsArray[start] != numsArray[end]:
                return False
            else:
                start+=1
                end-=1
        return True            
                


           