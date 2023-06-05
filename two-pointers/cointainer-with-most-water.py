# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            waterContainer = (right - left) * min(height[left], height[right])
            res = max(res, waterContainer)

            if height[left] < height[right]:
                left += 1
                while left < right and height[left] == height[left - 1]:
                    left += 1
            else:
                right -= 1
                while right > left and height[right] == height[right + 1]:
                    right -= 1
            
        return res