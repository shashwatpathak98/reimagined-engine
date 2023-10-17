class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        for character in string:
            length = len(stack)
            if character in dictionary:
                if length is 0:  
                    lastcharacter = "!"                    
                if length is not 0:
                    lastcharacter = stack.pop() 
                if dictionary[character] is not lastcharacter:  
                    return False       
            else:
                stack.append(character)  
                
        return len(stack) is 0





               
