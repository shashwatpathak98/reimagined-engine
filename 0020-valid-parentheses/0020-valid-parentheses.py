class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}    
        for character in string: 
            if character in dictionary:
                lastcharacter = stack.pop() if length_hint(stack) != 0  else " "  
                if dictionary[character] != lastcharacter: return False
            else:
                stack.append(character)  
                
        return len(stack) == 0





               
