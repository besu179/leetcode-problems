class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(arr)

        while n > 1:
            max_index = arr[:n].index(max(arr[:n]))

            if max_index != n - 1:
                if max_index != 0:
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                    ans.append(max_index + 1)
                ans.append(n)
                arr[:n] = arr[:n][::-1]
            n -= 1
            
        return ans