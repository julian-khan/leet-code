# https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Sorted = sorted(s1)

        for i in range(len(s2) - len(s1) + 1):
            s2Subtring = sorted(s2[i:i+len(s1)])

            if s2Subtring == s1Sorted:
                return True
        
        return False