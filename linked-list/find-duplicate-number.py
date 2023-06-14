# https://leetcode.com/problems/find-the-duplicate-number/

#Time complexity O(n), space complexity O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Using Floyd's Cycle Detection algorithm
        slow = fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        secondSlow = 0
        while True:
            secondSlow = nums[secondSlow]
            slow = nums[slow]

            if secondSlow == slow:
                return secondSlow