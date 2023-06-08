# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        #Using the stack to only store indexes to reduce memory usage
        stack.append(0)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                targetIndex = stack.pop()
                res[targetIndex] = i - targetIndex
            
            stack.append(i)

        return res
