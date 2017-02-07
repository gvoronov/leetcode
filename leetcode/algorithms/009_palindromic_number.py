class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x >= 0:
            x = str(x)
            solution = True
            for i in range(len(x) / 2):
                if x[i] != x[-i - 1]:
                    solution = False

            return solution

        else:
            return False
