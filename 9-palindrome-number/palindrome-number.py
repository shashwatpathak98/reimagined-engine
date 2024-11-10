class Solution:
    def isPalindrome(self, x: int) -> bool:
        
         num = str(x)
         revNum = num[::-1]
         if num == revNum:
            return True
         else:
            return False   