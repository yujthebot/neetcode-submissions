class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result= []
        seen = set()
        def perm(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in seen:
                    path.append(nums[i])
                    seen.add(nums[i])
                    perm(path)
                    path.pop()
                    seen.remove(nums[i])
        perm([])
        return result
