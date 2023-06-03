# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class TwoSumLocator:
    def __init__TwoSumLocater(self):
        l, r = 0, len(arr) - 1
    
    def binarySearch(self, arr, start, target):

        l, r = start, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        twoSumLocator = TwoSumLocator

        for i in range(len(numbers)-1):
            req = target - numbers[i]

            foundInd = twoSumLocator.binarySearch(self, numbers, i + 1, req)

            if foundInd != -1:
                return [i + 1, foundInd + 1]