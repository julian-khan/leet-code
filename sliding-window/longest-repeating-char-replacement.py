# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxCount = 0
        counts = {}
        left = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxCount = max(maxCount, counts[s[right]])

            if (right - left + 1) - maxCount > k:
                counts[s[left]] -= 1
                left += 1
            else:
                res = max(res, right - left + 1)
            
        return res