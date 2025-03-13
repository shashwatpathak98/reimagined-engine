class Solution:
    def isValid(self, s: str) -> bool: 

        stack = []
        for c in s:
            if len(stack) == 0 or c in ['(','{','[']:
                stack.append(c)
            else:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == '[':
                    stack.pop()
                else:
                    return False    
        return len(stack) == 0                


                        

        