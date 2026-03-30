class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count != 0:
                heapq.heappush_max(heap, (count, char))
        heapq.heapify_max(heap)

        res = ""
        while heap:
            count, char = heapq.heappop_max(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    return res

                count2, char2 = heapq.heappop_max(heap)
                res += char2
                count2 -= 1

                if count2 != 0:
                    heapq.heappush_max(heap, (count2, char2))
            else:
                res += char
                count -= 1
            if count != 0:
                heapq.heappush_max(heap, (count, char))
        return res

