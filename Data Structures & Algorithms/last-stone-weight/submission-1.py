class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >1:
            n1 = heapq.heappop_max(stones)
            n2 = heapq.heappop_max(stones)
            if n1 - n2 == 0:
                pass
            else:
                heapq.heappush_max(stones,n1-n2) 
        return stones[0] if stones !=[] else 0