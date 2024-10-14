class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        bestBuy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > bestBuy:
                maxPro = max(maxPro, prices[i]-bestBuy)
            bestBuy = min(bestBuy, prices[i])
        return maxPro 