class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        ans = 0
        prev = points[0]

        for point in points[1:]:
            ans = max((point[0] - prev[0]), ans)
            prev = point
        return ans