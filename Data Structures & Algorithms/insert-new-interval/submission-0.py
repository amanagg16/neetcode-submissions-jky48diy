class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        n = len(intervals)
        res = []
        while index < n:
            if newInterval[0] <= intervals[index][0]:
                if res[-1][1] >= newInterval[0]: # overlap
                    res[-1] = [res[-1][0], max(res[-1][1], newInterval[1])]
                else:
                    res.append(newInterval)
                break
            else:
                res.append(intervals[index])
                index += 1
            
        while index < n:
            if intervals[index][0] <= res[-1][1]:
                res[-1] = [res[-1][0],max(res[-1][1], intervals[index][1])]
            else:
                res.append(intervals[index])
            index += 1
            
        return res