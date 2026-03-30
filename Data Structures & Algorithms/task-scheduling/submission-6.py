class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [c for c in count.values()]
        time = 0
        q = deque()

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop_max(heap) - 1

                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])
        return time