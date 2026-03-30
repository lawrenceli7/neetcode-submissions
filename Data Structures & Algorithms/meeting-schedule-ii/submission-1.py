"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # two sorted arrays, start and end time
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # res is the max for the count variable
        # count to keep track of start and end times of meetings
        res, count = 0, 0
        # current positions for our start and end arrays
        s, e = 0, 0

        while s < len(intervals):
            # if position at start less than position at end array
            if start[s] < end[e]:
                # increment start by 1
                s += 1
                # increment count by 1 (one additional meeting going on)
                count += 1
            # if the end array position is greater than or equal to the start array position
            else:
                # increment end array by 1
                e += 1
                # decrement count by 1
                count -= 1
            # update res
            res = max(res, count)
        return res



