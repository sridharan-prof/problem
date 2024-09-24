class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            column_row = [1] * (i + 1)
             
            for j in range(1, i):
                column_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(column_row)
        return triangle 
        