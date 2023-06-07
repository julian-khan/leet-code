# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l, r = 0, 0
        while r < len(nums):
            if q and l > q[0]:
                q.popleft()

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            r += 1       
        return res