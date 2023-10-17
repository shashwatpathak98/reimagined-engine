class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        for character in string:
            if character in dictionary:
                if len(stack) is 0:  
                    lastcharacter = "!"                    
                if len(stack) is not 0:
                    lastcharacter = stack.pop() 
                if dictionary[character] is not lastcharacter:  
                    return False       
            else:
                stack.append(character)  
                
        return len(stack) is 0





               
