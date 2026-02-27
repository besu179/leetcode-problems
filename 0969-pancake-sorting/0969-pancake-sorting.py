class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(arr)

        while n > 1:
            max_idx = arr.index(max(arr[:n]))

            if max_idx != n - 1:
                if max_idx != 0:
                    ans.append(max_idx + 1)
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                
                ans.append(n)
                arr[:n] = arr[:n][::-1]
            
            n -= 1
            
        return ans