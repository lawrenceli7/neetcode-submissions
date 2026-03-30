class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        res = 0

        for start, end in intervals[1:]:
            if start >= intervals[0][1]:
                intervals[0][1] = end
            else:
                res += 1
                intervals[0][1] = min(intervals[0][1], end)
        return res
