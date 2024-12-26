class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        # carry = 0
        # for index in range(len(digits) - 1, -1, -1):
        #     if index == len(digits) - 1:
        #         digits[index] += 1
        #         if digits[index] > 9:
        #             digits[index] = 0
        #             carry = 1
        #     else:
        #         if carry == 1:
        #             digits[index] += 1
        #             if digits[index] > 9:
        #                 digits[index] = 0
        #                 carry = 1
        #             else:
        #                 carry = 0

        # return digits if carry == 0 else [carry] + digits
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

                if digits[i] > 9:
                    carry = 1
                    digits[i] = 0

            else:
                if carry == 1:
                    digits[i] += 1
                    
                    if digits[i] > 9:
                        carry = 1
                        digits[i] = 0
                    else:
                        carry = 0
        return digits if carry == 0 else [carry]+digits                 
