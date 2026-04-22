class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def possible(capacity):
            d = 1
            cur_load = 0

            for w in weights:
                if cur_load + w > capacity:
                    d += 1
                    cur_load = w
                else: cur_load += w

            return d <= days

        mx, mn = sum(weights), max(weights)

        mid = (mx + mn) // 2

        while mx > mn:
            mid = (mx + mn) // 2

            if possible(mid):
                mx = mid
            else:
                mn = mid + 1
        return mn