class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        ans = 0

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                ans = max(ans, height * (i - index))
                start = index

            stack.append((heights[i], start))

        while stack:
            height, index = stack.pop()
            ans = max(ans, height * (len(heights) - index))

        return ans