class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = Counter(bin(n)[2:])
        return num["1"]