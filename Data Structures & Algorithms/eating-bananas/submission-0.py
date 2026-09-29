class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo<hi:
            mid = (lo+hi)//2
            if self.valid_range(h,piles,mid):
                hi = mid
            else:
                lo = mid+1
        return lo
    def valid_range(self,h,piles,rate):
        s = 0
        for p in piles:
            s += (p+rate-1)//rate
        if s <= h:
            return True
        else: 
            return False
            
            
            