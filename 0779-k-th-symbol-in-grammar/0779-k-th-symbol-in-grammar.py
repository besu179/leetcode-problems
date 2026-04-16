class Solution(object):
    def recursion(self, n, k):
        if n == 1:
            return 0

        total_elements = 2 ** (n - 1)
        half_elements = total_elements // 2

        if k > half_elements:
            return 1 - self.recursion(n, k - half_elements)

        return self.recursion(n - 1, k)

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.recursion(n, k)