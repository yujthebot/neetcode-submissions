class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # cannot sort as it breaks the position
        if sum(nums) < target:
            return 0
        l = 0
        r = 0
        Csum = 0
        minL = len(nums)
        while r<len(nums):
            Csum += nums[r]
            r+=1
            while Csum >=target:
                minL = min(minL, r-l)
                Csum -= nums[l]
                l+=1
        return minL
