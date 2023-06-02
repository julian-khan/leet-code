# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedWord = ''

        for char in s:
            if char.isalnum():
                strippedWord += char.lower()
        
        start = 0
        end = len(strippedWord) - 1

        while start < end:
            if strippedWord[start] != strippedWord[end]:
                return False
            start += 1
            end -= 1

        return True