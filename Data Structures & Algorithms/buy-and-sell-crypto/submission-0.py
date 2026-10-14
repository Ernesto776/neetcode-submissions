class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mostProfit = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                profit = prices[sell] - prices[buy]
                if profit > mostProfit:
                    mostProfit = profit
        return mostProfit