class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def possible(val):
            t = 0

            for pile in piles:
                t += (pile + val - 1) // val

            return t <= h

        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            if possible(mid):
                r = mid - 1
            else: l = mid + 1
        return l