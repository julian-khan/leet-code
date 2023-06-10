# https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)

        left, right = 1, minK

        while left <= right:
            eatingRate = (left + right) // 2
            eatingTime = 0

            for n in piles:
                eatingTime += math.ceil(n / eatingRate)

            if eatingTime <= h:
                minK = min(minK, eatingRate)
                right = eatingRate - 1
            else:
                left = eatingRate + 1

        return minK