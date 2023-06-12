# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalNumLength = len(nums1) + len(nums2)
        halfTotalNumLength = totalNumLength // 2

        numberList1 = nums1 if len(nums1) <= len(nums2) else nums2
        numberList2 = nums2 if numberList1 == nums1 else nums1

        l, r = 0, len(numberList1) - 1

        while True:
            mid = (l + r) // 2
            numberList1Left = numberList1[mid] if mid >= 0 else float('-inf')
            numberList1Right = numberList1[mid + 1] if mid + 1 < len(numberList1) else float('inf')
            
            #Determining the second list's left partition limit
            targetIndex = halfTotalNumLength - (mid + 1) - 1
            numberList2Left = numberList2[targetIndex] if targetIndex >= 0 else float('-inf')
            numberList2Right = numberList2[targetIndex + 1] if targetIndex + 1 < len(numberList2) else float('inf')

            if numberList1Left <= numberList2Right and numberList2Left <= numberList1Right:
                if totalNumLength % 2 != 0:
                    return min(numberList1Right, numberList2Right)
                return (max(numberList1Left, numberList2Left) + min(numberList1Right, numberList2Right)) / 2
            elif numberList1Left > numberList2Right:
                r = mid - 1
            else:
                l = mid + 1