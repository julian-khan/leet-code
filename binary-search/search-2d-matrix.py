# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Perform binary search to locate the row containing the target value
        l, r = 0, len(matrix) - 1
        mid = -1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            else:
                l = mid + 1
        
        # The value of mid is the index of the correct row
        #Perform binary search on the row containing the target to locate the index
        targetRow = matrix[mid]
        left, right = 0, len(targetRow) - 1

        while left <= right:
            middle = (left + right) // 2

            if targetRow[middle] > target:
                right = middle - 1
            elif targetRow[middle] < target:
                left = middle + 1
            else:
                return True
        
        return False
