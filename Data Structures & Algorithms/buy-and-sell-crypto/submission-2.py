class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mi = prices[0]
        for i in range(len(prices)):
            mi = min(prices[i], mi)
            profit = prices[i] - mi
            res = max(res, profit)
        return res