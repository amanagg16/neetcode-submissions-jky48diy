from heapq import heappush, heappop, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        
        n = len(tasks)
        tasks.sort(key=lambda task:(task[0]))

        heap = []
        
        time = tasks[0][0]
        i = 0
        output = []
        while i < n or heap:
            
            while i < n and time >= tasks[i][0]:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not heap and i < n:
                time = tasks[i][0]
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            while heap:
                proc_time , index = heappop(heap)
                time += proc_time
                output.append(index)
            

        return output