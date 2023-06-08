# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        stack.append(temperatures[0])

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                targetIndex = stack.pop()[1]
                res[targetIndex] = i - targetIndex
            
            stack.append(tuple(temperatures[i], i))

        return res

sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]
Solution.dailyTemperatures(self, temperatures)