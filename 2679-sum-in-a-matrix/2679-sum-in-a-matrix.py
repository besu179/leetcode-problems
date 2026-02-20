class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        score = 0
        rows = len(nums)
        cols = len(nums[0])
        for r in range(rows):
            nums[r].sort().
        matrix = [[0] * rows for _ in range(cols)] 
        for row in range(rows):
            for col in range(cols):
                matrix[col][row] = nums[row][col]
        for row in matrix:
            score += max(row)
            
        return score
#sorted each row, traverse the matrix and add the maximum of each row to the score