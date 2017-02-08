class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        palindromes = list()

        # search for starting even (2-)palindromes
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                palindromes.append([i, i+1])

        # search for starting odd (3-)palindromes
        for i in range(1, len(s) - 1):
            if s[i-1] == s[i+1]:
                palindromes.append([i-1, i+1])

        # Check for situtation of only 1-palindromes and zero length strings
        if len(palindromes) == 0:
            return s[0]

        keep_looking = True
        while keep_looking:
            keep_looking = False
            for i, (i1, i2) in enumerate(palindromes):
                if i1 != 0 and i2 != len(s) - 1:
                    if s[i1 - 1] == s[i2 + 1]:
                        keep_looking = True
                        palindromes[i] = [i1 - 1, i2 + 1]

        max_len, max_palindrome = 0, ''
        for i1, i2 in palindromes:
            if i2 - i1 > max_len:
                max_palindrome = s[i1:i2+1]
                max_len = i2 - i1

        return max_palindrome
        
