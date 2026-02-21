class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        ans = 0
        for b in num:
            if b == "1":
                ans += 1
        return ans