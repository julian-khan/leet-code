# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        increasingHeights = []

        for i in range(len(heights)):
            startIndex = i
            while increasingHeights and increasingHeights[-1][0] > heights[i]:
                height, startIndex = increasingHeights.pop()
                maxArea = max(maxArea, height * (i - startIndex))

            increasingHeights.append((heights[i], startIndex))

        for hgt, ind in increasingHeights:
            maxArea = max(maxArea, hgt * (len(heights) - ind))
        
        return maxArea