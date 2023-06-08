# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        stack.append((temperatures[0], 0))

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                targetIndex = stack.pop()[1]
                res[targetIndex] = i - targetIndex
            
            stack.append((temperatures[i], i))

        return res
