class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        final = []
        for a1 in range(n-2):
            for a2 in range(a1+1,n-1):
                l = a2+1
                r = n-1
                while l<r:
                    condition = nums[a1] + nums[a2]+ nums[l] + nums[r]
                    sets = [nums[a1], nums[a2], nums[l], nums[r]]
                    
                    if condition == target:
                        if tuple(sets) not in seen:
                            final.append(sets)
                            seen.add(tuple(sets))
                        l+=1
                        r-=1
                    elif condition > target:
                        r-=1
                    elif condition < target:
                        l+=1
        return final

        