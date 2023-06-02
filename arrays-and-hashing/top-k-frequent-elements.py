# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1

        for num, freq in numToFreq.items():
            freqs[freq].append(num)
        
        i = len(freqs) - 1
        while i > 0 and k > 0:
            for n in freqs[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
            i -= 1
            
        

        

