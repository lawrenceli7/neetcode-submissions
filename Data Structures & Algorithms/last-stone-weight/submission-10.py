class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        heapq.heapify_max(stones)

        while len(stones) > 1:
            firstLargest = heapq.heappop_max(stones)
            secondLargest = heapq.heappop_max(stones)

            if firstLargest != secondLargest:
                heapq.heappush_max(stones, firstLargest - secondLargest)
        return stones[0] if len(stones) == 1 else 0