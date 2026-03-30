class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if end value of new interval is less than start value at current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new interval start value is greater than the end vlaue of current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapping intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0])
                , max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
