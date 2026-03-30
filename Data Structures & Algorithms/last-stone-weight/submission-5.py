class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            secondLargest = heapq.heappop(stones)

            if largest != secondLargest:
                heapq.heappush(stones, largest - secondLargest)
        return abs(stones[0]) if len(stones) == 1 else 0