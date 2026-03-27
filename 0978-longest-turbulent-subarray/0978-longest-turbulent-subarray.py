class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(A)        
        ans = 1
        l = 0
        def get_comp(a, b):
            if a < b: return 0
            if a > b: return 1
            return -1

        for r in range(1, n):
            c = get_comp(A[r-1], A[r])
            if c == -1:
                l = r
            elif r > 1 and c == get_comp(A[r-2], A[r-1]):
                l = r - 1
            ans = max(ans, r - l + 1)
        return ans