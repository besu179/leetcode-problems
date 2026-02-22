class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
            
        arr = [[] for i in range(numRows)]
        step = 1
        num = 0
        for i in range(len(s)):
            arr[num].append(s[i])
            if num == numRows -1:
                step = -1
            elif num == 0:
                step = 1
            num += step
        ans = ""
        for i in range(len(arr)):
            ans += "".join(arr[i])
        return ans