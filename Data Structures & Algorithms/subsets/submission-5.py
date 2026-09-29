class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, current):
            result.append(current[:])

            for j in range(i, len(nums)):
                current.append(nums[j])
                backtrack(j + 1, current)
                current.pop()

        backtrack(0, [])

        return result
        # n = len(nums)
        # remove  = n-2
        # for i in range(n):
        #     for j in range(n-i):
        #         flist.append(nums[i:i+j+1])
        #     #Apply a backtrack idea
        # return flist


