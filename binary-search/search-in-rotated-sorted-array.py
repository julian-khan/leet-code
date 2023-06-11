# https://leetcode.com/problems/search-in-rotated-sorted-array/

#Approach 1 - use nested conditional statements to determine the partition of the array to continue
#binary search on

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return - 1

#Approach 2 - find the minimum element in the array (the rotation index) and then use
#binary search on the relevant partition of the array
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
        
        


