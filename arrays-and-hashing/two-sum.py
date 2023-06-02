# https://leetcode.com/problems/two-sum/

# Version 1 with map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = { target - nums[i] : i for i in range(len(nums))}
        
        for i in range(len(nums)):
            if nums[i] in map and i != map[nums[i]]:
                return [i, map[nums[i]]]


#Version 2 with nested for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]