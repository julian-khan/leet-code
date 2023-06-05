# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        res = 1
        l, r = 0, 1

        seen.add(s[l])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
                
            else:
                while l < r and s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                r += 1
                
        return res