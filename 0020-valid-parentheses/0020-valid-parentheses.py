class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}    
        for character in string: 
            if character in dictionary:
                lastcharacter = stack.pop() if len(stack) != 0  else  stack.append(" ")  
                if dictionary[character] != lastcharacter: return
            else:
                stack.append(character)  
                
        return len(stack) == 0





               
