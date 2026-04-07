class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        ans = 0

        for log in logs:
            if log == "../":
                if ans > 0:
                    ans -= 1
            elif log == "./":
                continue
            else:
                ans += 1
        return ans                 