class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = res = 0
        prefix_count = {0:1}

        for num in nums:
            prefix_sum += num
            diff = prefix_sum-k

            res += prefix_count.get(diff, 0)
            prefix_count[prefix_sum] = 1 + prefix_count.get(prefix_sum, 0)
        
        return res