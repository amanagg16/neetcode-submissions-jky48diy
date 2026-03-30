# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, start, mid, end):
        temp = []

        l, r = start, mid+1
        while l<=mid and r<=end:
            if arr[l].key > arr[r].key:
                temp.append(arr[r])
                r += 1
            else:
                temp.append(arr[l])
                l += 1

        while l <= mid:
            temp.append(arr[l])
            l += 1
        while r <= end:
            temp.append(arr[r])
            r += 1

        l = start
        for n in temp:
            arr[l] = n
            l += 1

    def _mergeSort(self, arr, start, end):

        if start >= end:
            return
        
        mid = math.floor((start + end)/2)

        self._mergeSort(arr, start, mid)
        self._mergeSort(arr, mid+1, end)
        self.merge(arr, start, mid, end)


        
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self._mergeSort(pairs, 0, len(pairs)-1)
        return pairs