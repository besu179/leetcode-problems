class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])

        ans = [[0] * cols for _ in range(rows)] #ans new matrix that have the same dimension with the img given

        for row in range(rows): #for each rows
            for col in range(cols): #for each columns, here one element will be selected and average with it's surrounding will be calculated
                total = 0
                count = 0

                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if i < 0 or j < 0 or i >= rows or j >= cols:
                            continue
                        total += img[i][j]
                        count += 1
                ans[row][col] = total // count
        return ans