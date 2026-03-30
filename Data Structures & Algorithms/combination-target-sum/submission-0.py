from typing import List

class Solution:
    def combinationSum(self, candidates:List[int], target:int)->List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            # if we go beyond the array or go beyond the total..we return

            if total == target:
                res.append(cur.copy())
                return
            # the above condition is there because in subsets we could only stop at the end...but here we can stop once the target is acheived
            
            # pick and recur for same
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()

            # not pick and recur for next
            dfs(i+1, cur, total)


        
        dfs(0, [], 0)
        return res