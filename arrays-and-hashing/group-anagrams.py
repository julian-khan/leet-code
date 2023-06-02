# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict()
        for word in strs:
            sortedWord = tuple(sorted(word))
            anagrams.setdefault(sortedWord, []).append(word)
        
        outputList = []
        for anagramGroup in list(anagrams.values()):
            outputList.append(anagramGroup)
        
        return outputList
