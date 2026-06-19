from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bs = { ")" : "(", "]" : "[", "}" : "{" }
        

        for char in s:
            if char in bs:
                if stack and   stack[-1] == bs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
            
                





        