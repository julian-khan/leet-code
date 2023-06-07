# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
            stack.pop()
        
        return True if not stack else False