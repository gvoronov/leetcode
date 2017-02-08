class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # solution = 0

        str = str.lstrip(' ')

        if str == '':
            return 0

        if str[0] == '-':
            neg = True
            str = str[1:]
        elif str[0] == '+':
            neg = False
            str = str[1:]
        else:
            neg = False

        solution = list()
        for c in str:
            if not c.isdigit():
                break

            solution.append(c)

        if len(solution) == 0:
            return 0
        else:
            solution = int(''.join(solution))
            if neg:
                return max(-solution, -2147483648)
            else:
                return min(solution, 2147483647)


                
