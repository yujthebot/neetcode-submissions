class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        ans = []
        for i, ch in enumerate(nums):
            table[ch] = table.get(ch,0)+1
        maxs = list(table.values())
        maxs.sort(reverse = True)
        for j in range(len(table.values())-k):
            maxs.pop()
        for key, values in table.items():
            if values in maxs:
                ans.append(key)
        return ans