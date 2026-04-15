class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        ans = self.generate(numRows - 1)
        new_row = [1] * numRows

        for i in range(1, numRows - 1):
            new_row[i] = ans[-1][i - 1] + ans[-1][i]
        ans.append(new_row)

        return ans