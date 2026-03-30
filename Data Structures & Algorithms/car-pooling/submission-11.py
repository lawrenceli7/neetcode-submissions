class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        trips.sort(key=lambda t: t[1])
        currPass = 0

        for numPass, start, end in trips:
            while heap and heap[0][0] <= start:
                currPass -= heap[0][1]
                heapq.heappop(heap)

            currPass += numPass
            if currPass > capacity:
                return False
            heapq.heappush(heap, (end, numPass))
        return True