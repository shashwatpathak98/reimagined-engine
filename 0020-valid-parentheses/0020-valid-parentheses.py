class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        string = s
        empty = 0
        for character in string:
            if character in dictionary:
                if len(stack) is empty:  
                    lastcharacter = "!"                    
                if len(stack) is not empty:
                    lastcharacter = stack.pop() 
                if dictionary[character] is not lastcharacter:  
                    return False       
            else:
                stack.append(character)  
                
        return len(stack) is empty





               
