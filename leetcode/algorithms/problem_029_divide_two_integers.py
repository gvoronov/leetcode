class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        a, b = 0, 0

        while a <= abs(dividend):
            a += abs(divisor)
            b += 1

        if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >= 0):
            factor = 1
        else:
            factor = -1
        return factor * (b - 1)

if __name__ == "__main__":
    print Solution().divide(10, 3)
    print Solution().divide(9, 3)
    print Solution().divide(0, 3)
