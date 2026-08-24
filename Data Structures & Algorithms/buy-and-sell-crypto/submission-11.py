class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        max_Profit = 0
        for price in prices:
            min_price=min(min_price,price)
            max_Profit=max(max_Profit,price-min_price)
        return max_Profit