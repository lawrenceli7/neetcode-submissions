class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(heap, (count, char))
        
        res = ""
        while heap:
            count, char = heapq.heappop(heap) 
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    return res
                
                count2, char2 = heapq.heappop(heap)
                res += char2
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
            else:
                res += char
                count += 1
            if count != 0:
                heapq.heappush(heap, (count, char))
        return res