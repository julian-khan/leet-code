# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subRes = []

        def dfs(self, n, open, closed):
            if open > n:
                return

            if len(subRes) == n * 2:
                res.append(''.join(subRes))
                return
            
            if open < n:
                subRes.append('(')
                dfs(self, n, open + 1, closed)
                subRes.pop()

            if closed < open:
                subRes.append(')')
                dfs(self, n, open, closed + 1)
                subRes.pop()
        
        dfs(self, n, 0, 0)

        return res
