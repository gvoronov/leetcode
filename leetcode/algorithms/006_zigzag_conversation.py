class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows <= 1:
            return s

        rows = [''] * numRows
        for i, c in enumerate(s):
            pos = i % (2 * numRows - 2)

            if pos < numRows:
                rows[pos] = rows[pos] + c
            else:
                row = 2 * numRows - pos - 2
                rows[row] = rows[row] + c

        solution = ''
        for row in rows:
            solution += row

        return solution
                
