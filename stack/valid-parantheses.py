# https://leetcode.com/problems/valid-parentheses/

#A more optimised solution than my original version for both run time and memory usage

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {
            '(': ')',
            '[': ']',
            '{': '}'
            }

        for char in s:
            if char in charMap:
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
        
        return not stack