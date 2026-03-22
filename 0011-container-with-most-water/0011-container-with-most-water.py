class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = l = width = 0
        r = len(height) - 1

        while l < r:
            min_height = min(height[l], height[r])
            width = r - l

            vol = max(min_height * width, vol)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return vol