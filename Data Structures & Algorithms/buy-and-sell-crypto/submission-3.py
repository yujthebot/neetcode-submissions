class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = []
        for i in range(len(prices)):
            m = max(prices[i:])
            dif.append(m-prices[i])
        return max(dif)