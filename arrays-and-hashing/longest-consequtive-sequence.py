# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(set(nums)) == 1:
            return 1

        sortedNums = sorted(nums)
        res = 1

        counter = 1
        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i-1]:
                continue
            if sortedNums[i-1] == sortedNums[i] - 1:
                counter += 1
                res = max(res, counter)
            else:
                counter = 1

        return res