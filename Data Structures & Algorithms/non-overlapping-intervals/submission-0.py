class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by starting time, look at adjacent intervals
        # know they are overlapping when current interval start time is less than previous interval end time
        # remove the one with the largest end value, and keep the minimum one

        intervals.sort(key = lambda pair : pair[0])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res