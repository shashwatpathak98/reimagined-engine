class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in dictionary:
                if stack:  
                    lastelement = stack.pop() 
                else:
                    lastelement = "#"  
                
                if dictionary[i] != lastelement:  
                    return False
            else:
                stack.append(i)  
                
        return not stack  




               
