class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        ans = []
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] >= interval[0] >= prev[0]:
                ans.append([prev[0], interval[1]])
                prev = [prev[0], interval[1]]
            else:
                ans.append(interval)
                prev = interval
        return ans