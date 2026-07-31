class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        output = [0]*n
        for i in range(n-1, -1, -1):
            ele = temperatures[i]
            while s and temperatures[s[-1]] < ele:
                s.pop()
            

            if s:
                output[i] = s[-1] - i
            
            s.append(i)
            
        return output