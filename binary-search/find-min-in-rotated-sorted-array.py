# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                minVal = min(minVal, nums[mid])
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1

        return minVal
