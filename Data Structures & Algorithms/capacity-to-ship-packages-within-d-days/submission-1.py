class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = sum(weights)

        def canShip(capacity):
            daysUsed = 1
            currCap = capacity

            for w in weights:
                if currCap - w < 0:
                    daysUsed += 1
                    currCap = capacity
                currCap -= w
            return daysUsed <= days

        while left <= right:
            middle = (left + right) // 2

            if canShip(middle):
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1
        return res