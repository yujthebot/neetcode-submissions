class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[mid]: #left side is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:     #right side is sorted
                if nums[mid]< target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1


        return -1