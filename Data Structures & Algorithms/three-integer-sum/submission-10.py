class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create initial loop for middle element

        nums.sort()
        
        ans = []
        for mid in range(1,len(nums)-1):
            left= 0
            right =len(nums)-1
            while left<mid and mid<right:
                s = nums[left] + nums[mid] + nums[right]
                if s == 0:
                    triplet = sorted([nums[left], nums[mid], nums[right]])
                    if triplet not in ans:
                        ans.append(triplet)
                    left+=1
                    right-=1
                elif s< 0:
                    left+=1
                elif s>0:
                    right-=1
        return ans