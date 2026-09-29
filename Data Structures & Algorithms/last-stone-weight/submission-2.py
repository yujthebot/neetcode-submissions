class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: #solution without using heap_max type of functions
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)
            if n1 - n2 == 0:
                pass
            else:
                heapq.heappush(stones, n1-n2)
        return -stones[0] if stones !=[] else 0
        