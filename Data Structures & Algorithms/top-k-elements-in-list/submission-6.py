class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        ans = []
        for i, ch in enumerate(nums):
            table[ch] = table.get(ch,0)+1
        maxs = sorted(list(table.values()),reverse = True)[:k]
        for key, values in table.items():
            if values in maxs:
                ans.append(key)
        return ans