class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001

        for numPass, start, end in trips:
            passChange[start] += numPass
            passChange[end] -= numPass
        
        currPass = 0
        for i in range(1001):
            currPass += passChange[i]
            if currPass > capacity:
                return False
        return True
        
        
        # trips.sort(key=lambda t: t[1])
        # heap = [] # (end, numPass)
        # currPass = 0

        # for numPass, start, end in trips:
        #     # trip has been completed
        #     while heap and heap[0][0] <= start:
        #         # decrement num of passengers
        #         currPass -= heap[0][1]
        #         heapq.heappop(heap)
                
        #     currPass += numPass
        #     if currPass > capacity:
        #         return False
        #     heapq.heappush(heap, (end, numPass))
        # return True