class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        r = int(c ** 0.5)
        l = 0
        while l <= r:
            val = l * l + r * r
            if val == c:
                return True
            elif val > c:
                r -= 1
            else:
                l += 1
        return False