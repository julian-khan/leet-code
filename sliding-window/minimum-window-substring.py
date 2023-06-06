# https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t:
            return s
        elif len(s) < len(t):
            return ""
        elif t in s:
            return t

        if len(s) == len(t):
            if sorted(t) == sorted(s):
                return s
            else:
                return ""

        res = None
        tMap = {}
        sMap = {}
        l, r = 0, len(t) - 1

        for char in t:
            tMap[char] = tMap.get(char, 0) + 1

        for i in range(len(t)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1

        while r < len(s):
            for key, val in tMap.items():
                while sMap.get(key, 0) < val:
                    r += 1
                    if r > len(s) - 1:
                        return res if res else ""
                    sMap[s[r]] = sMap.get(s[r], 0) + 1

            if not res or r - l + 1 < len(res):
                res = s[l:r+1]
            
            while l < r:
                sMap[s[l]] -= 1
                l += 1
                
                if s[l-1] in tMap and tMap[s[l-1]] > sMap[s[l-1]]:
                    break
                else:
                    if not res or r - l + 1 < len(res):
                        res = s[l:r+1]

        return res if res else ""