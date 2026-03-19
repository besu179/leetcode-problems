class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        hm = defaultdict(int)
        l = ans = 0

        for r in range(len(fruits)):
            hm[fruits[r]] = hm.get(fruits[r], 0) + 1

            while len(hm) > 2:
                hm[fruits[l]] -= 1
                if hm[fruits[l]] == 0:
                    del hm[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)
        return ans