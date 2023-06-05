# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = inf

        for price in prices:
            buyPrice = min(buyPrice, price)
            profitIncrement = price - buyPrice

            profit = max(profit, profitIncrement)
            
        return profit