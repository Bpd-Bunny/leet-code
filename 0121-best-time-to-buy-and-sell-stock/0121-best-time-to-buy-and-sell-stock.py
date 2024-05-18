class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        right = prices[n-1]
        profit = 0
        for i in range(n-1,-1,-1):
            curr_p = right - prices[i]
            if curr_p > profit and curr_p>0:
                profit = curr_p
            else:
                right = max(right, prices[i])
        return profit
