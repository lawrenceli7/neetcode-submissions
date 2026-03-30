"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = sorted([i.start for i in intervals])
        endTime = sorted([i.end for i in intervals])

        res, count = 0, 0
        start, end = 0, 0

        while start < len(intervals):
            if startTime[start] < endTime[end]:
                count += 1
                start += 1
            else:
                count -= 1
                end += 1
            res = max(res, count)
        return res