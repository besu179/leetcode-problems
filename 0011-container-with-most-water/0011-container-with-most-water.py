class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = 0
        left = len(height) - 1
        width = 0
        vol = 0

        while right < left:
            min_height = height[left] if height[right] > height[left] else height[right]
            width = left - right
            
            new_vol = min_height * width
            if new_vol > vol:
                vol = new_vol
            if height[right] > height[left]:
                left -= 1
            else:
                right += 1

        return vol