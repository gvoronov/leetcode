class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = ''
        roman, num  = self.get_str(roman, num, 1000, 'M', 'V', None)
        roman, num  = self.get_str(roman, num, 100, 'C', 'D', 'M')
        roman, num  = self.get_str(roman, num, 10, 'X', 'L', 'C')
        roman, num  = self.get_str(roman, num, 1, 'I', 'V', 'X')

        return roman

    def get_str(self, rstr, num, pow_of_10, char1, char5, char10):
        num_chars = num / pow_of_10
        new_num = num - num_chars * pow_of_10

        if num_chars >= 0 and num_chars < 4:
            new_rstr = rstr + (char1 * num_chars)
        elif num_chars == 4:
            new_rstr = rstr + char1 + char5
        elif num_chars >= 5 and num_chars < 9:
            new_rstr = rstr + char5 + (char1 * (num_chars - 5))
        elif num_chars == 9:
            new_rstr = rstr + char1 + char10

        return new_rstr, new_num

if __name__ == "__main__":
    print Solution().intToRoman(3999)
