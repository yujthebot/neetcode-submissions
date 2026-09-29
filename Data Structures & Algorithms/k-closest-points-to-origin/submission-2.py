class Solution: # remove the idea of dictiinary completely and use a tuple
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distlist = []
        for p in points:
            dist = (p[0]**2+p[1]**2)**0.5
            distlist.append((-dist,p))
        heapq.heapify(distlist)
        while len(distlist)>k:
            heapq.heappop(distlist)
        for i in distlist:
            ans.append(i[1])
        return ans