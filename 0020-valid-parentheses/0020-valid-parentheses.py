class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in dictionary:
                if len(stack) != 0:  
                    lastelement = stack.pop() 
                else:
                    lastelement = "#"  
                
                if dictionary[i] != lastelement:  
                    return False
            else:
                stack.append(i)  
                
        return len(stack) == 0





               
