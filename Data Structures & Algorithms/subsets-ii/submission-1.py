class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start,path):
            temp = None
            result.append(path[:])
            for i in range(start,len(nums)):
                if nums[i] == temp:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                temp = path.pop()
        backtrack(0,[])
        return result
        