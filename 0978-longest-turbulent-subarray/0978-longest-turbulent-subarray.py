class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(A)
        l = 0
        ans = 1
        
        for r in range(1, n):
            if A[r] == A[r-1]:
                l = r
            elif r > 1 and (A[r-2] < A[r-1] < A[r] or A[r-2] > A[r-1] > A[r]):
                l = r - 1
            ans = max(ans, r - l + 1)
            
        return ans