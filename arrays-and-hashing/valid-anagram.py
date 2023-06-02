# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenWord1 = {}

        for char in s:
            if char not in seenWord1:
                seenWord1[char] = 1
            else:
                seenWord1[char] += 1
        
        for char in t:
            if char not in seenWord1:
                return False
            seenWord1[char] -= 1
            if seenWord1[char] < 0:
                return False
        
        for val in list(seenWord1.values()):
            if val != 0:
                return False
        
        return True
