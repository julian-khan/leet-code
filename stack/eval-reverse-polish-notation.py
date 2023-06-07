# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = set(['+', '-', '*', '/'])

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                exp1 = stack.pop()
                exp2 = stack.pop()

                if char == '+':
                    stack.append(exp2 + exp1)
                elif char == '-':
                    stack.append(exp2 - exp1)
                elif char == '*':
                    stack.append(exp2 * exp1)
                else:
                    stack.append(int(exp2 / exp1))
                    
        return stack[0]
