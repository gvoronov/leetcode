class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            a = -1
            x *= -1
        else:
            a = 1

        solution = list(str(x))
        solution.reverse()
        solution = a * int(''.join(solution))

        if solution < -2**31 or solution > 2**31 - 1:
            return 0
        else:
            return solution
