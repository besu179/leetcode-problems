class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        ans = []
        for target in range(len(arr), 1, -1):
            idx = arr.index(target)
            
            if idx == target - 1:
                continue
            
            if idx != 0:
                ans.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            
            ans.append(target)
            arr[:target] = arr[:target][::-1]
        return ans