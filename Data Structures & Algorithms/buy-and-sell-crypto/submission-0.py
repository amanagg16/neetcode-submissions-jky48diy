class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = math.inf
        max_profit = 0

        for p in prices:
            if p < min_till_now:
                min_till_now = p
            else:
                max_profit = max(max_profit, p-min_till_now)
        
        return max_profit