class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        length = 0
        for n in nums:
            if n-1 not in numset:
                head = n
                length = 1
                while head+1 in numset:
                    head +=1
                    length += 1
            longest = max(longest, length)
        return longest
