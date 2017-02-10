class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for rstr, rval in [('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900)]:
            if rstr in s:
                num += rval
                s = s.replace(rstr, '')

        for rstr, rval in [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]:
            tmp_len = len(s)
            s = s.replace(rstr, '')
            num += rval * (tmp_len - len(s))

        return num

if __name__ == "__main__":
    print Solution().romanToInt('MMMCMXCIX')
