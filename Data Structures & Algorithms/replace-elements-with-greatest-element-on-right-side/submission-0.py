class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = []
        for i in range(len(arr)-1):
            l.append(max(arr[i+1:]))
        l.append(-1)
        return l