# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = 0 #index, value

        #To find the minimum element in the array and therefore the rotation degree
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < nums[minIndex]:
                minIndex = mid

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        #To determine the appropriate partition of the array to search
        if nums[minIndex] <= target <= nums[-1]:
            left, right = minIndex, len(nums) - 1
        elif nums[0] <= target <= nums[minIndex - 1]:
            left, right = 0, minIndex - 1
        else:
            return -1

        #Search the appropriate array partition
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return -1
        
        


