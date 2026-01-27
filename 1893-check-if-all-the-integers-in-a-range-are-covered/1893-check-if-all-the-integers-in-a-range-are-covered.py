class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left, right + 1):
            discovered = False
            for rng in ranges:
                if (rng[0] == rng[-1]) and rng[0] == i:
                    discovered = True
                    break
                elif i >= rng[0] and i <= rng[-1]:
                    discovered = True
                    break
            if not discovered:
                return False
        return discovered
        