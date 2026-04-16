class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        if k % 2:
            return self.kthGrammar(n - 1, (k + 1 )// 2)
        else:
            return 1 - self.kthGrammar(n - 1, (k + 1 )// 2)