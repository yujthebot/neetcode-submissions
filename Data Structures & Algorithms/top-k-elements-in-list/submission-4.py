class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        flist = []
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i] = 1
        klist = sorted(result.values(), reverse = True)[:k]
        for key, value in result.items():
            if value in klist:
                flist.append(key)
        return flist