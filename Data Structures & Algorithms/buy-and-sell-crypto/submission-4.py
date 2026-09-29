class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = []
        for i in range(n):
            m = max(prices[i:])
            diff.append(m-prices[i])
        return max(diff)