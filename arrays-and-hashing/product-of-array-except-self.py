# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [ 1 for i in range(len(nums))]
        fwdTotal = nums[0]
        backTotal = nums[-1]

        for i in range(1, len(nums)):
            res[i] = fwdTotal
            fwdTotal *= nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= backTotal
            backTotal *= nums[i]
        
        return res