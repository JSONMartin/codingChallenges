# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        def compare(i1, i2):
            if i1.start < i2.start:
                return -1
            elif i1.start > i2.start:
                return 1
            else:
                return 0

        intervals.sort(compare)

        new_intervals = []
        new_interval = intervals[0]

        for interval in intervals:
            if new_interval == False: new_interval = interval

            if new_interval.end > interval.start:
                new_interval.end = max(interval.end, new_interval.end)
            if new_interval.start > interval.start:
                new_interval.start = min(interval.start, new_interval.start)
            if new_interval.end < interval.start:
                new_intervals.append(new_interval)
                new_interval = interval

        new_intervals.append(new_interval)

        # print "----------------------------------------"
        # for interval in new_intervals:
        #     print("Interval Start:", interval.start)
        #     print("Interval end:", interval.end)

        return new_intervals


"""
TESTING
"""
s = Solution()

i1 = Interval(1, 3)
i2 = Interval(2, 6)
i3 = Interval(8, 10)
i4 = Interval(15, 18)
res = s.merge([i1, i2, i3, i4])

# i1 = Interval(1, 10)
# i2 = Interval(2, 9)
# i3 = Interval(3, 8)
# i4 = Interval(4, 7)
# i5 = Interval(5, 6)
# i6 = Interval(6, 6)

# res = s.merge([i1, i2, i3, i4, i5, i6])

