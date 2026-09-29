class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        ans = []
        print(nums)
        for j in range(1,n-1):
            i=0
            k=n-1
            while i<j and k>j:
                s= nums[i]+nums[j]+nums[k]
                if s == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    i+=1
                    k-=1
                elif s > 0:
                    k-=1
                elif s<0:
                    i+=1
        return ans

