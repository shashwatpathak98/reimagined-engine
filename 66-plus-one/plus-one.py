import numpy as np

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for index in range(len(digits)-1 , -1, -1):
            if index == len(digits) - 1:
                digits[index]+=1
                if digits[index] > 9:
                    digits[index] = 0
                    carry = 1
            else:
                if carry == 1:
                    digits[index]+= 1
                    if digits[index] > 9:
                        digits[index] = 0
                        carry = 1
                    else:
                        carry = 0    
        
        return digits if carry == 0 else [1]+digits
        
        


        