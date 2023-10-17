class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}      
        for character in string:
            lengthOfStack = len(stack)
            if character in dictionary:
                lastcharacter = stack.append(" ") if lengthOfStack is 0 else stack.pop()
                if dictionary[character] is not lastcharacter:  
                    return False       
            else:
                stack.append(character)  
                
        return (len(stack) == 0)





               
