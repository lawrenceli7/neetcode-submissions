class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(count, char) for char, count in count.items()]
        heapq.heapify_max(heap)
        res = ""
        prev = (0, "")

        if heap[0][0] > (len(s) + 1) // 2:
            return ""

        while heap:
            count, char = heapq.heappop_max(heap)
            res += char
            if prev[0] > 0:
                heapq.heappush_max(heap, prev)
            prev = (count - 1, char)
        return res
