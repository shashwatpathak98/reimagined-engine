class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        for character in string:
            if(stack != [] and character == ']' and stack[-1] == '['):
                stack.pop()
            elif(stack != [] and character == '}' and stack[-1] == '{'):
                stack.pop()
            elif(stack != [] and character == ')' and stack[-1] == '('):
                stack.pop()               
            else:
                stack.append(character)
        print(stack)        
        return stack == []                 


    





               
