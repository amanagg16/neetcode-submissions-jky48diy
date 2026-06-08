import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = math.inf
        def dfs(amt, no_of_coins):
            nonlocal res
            if amt == 0:
                res = min(res, no_of_coins)
                return

            for c in coins:
                if amt - c >= 0:
                    dfs(amt-c, no_of_coins+1)

        
        dfs(amount, 0)
        return res if res < math.inf else -1