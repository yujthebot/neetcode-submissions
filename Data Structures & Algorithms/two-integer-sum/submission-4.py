class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i,ch in enumerate(nums):
            table[ch] = i
        for i in range(len(nums)):
            b = target-nums[i]
            if b in table :
                ans = table[b]
                if ans != i:
                    break
        return [i,ans]