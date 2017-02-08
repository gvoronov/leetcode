class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if s == p:
            return True

        i, j = 0, 0
        while j < len(p):
            if j + 1 < len(p) and p[j + 1] == '*':
                if p[j] == '.':
                    num_pattern = len(s) - j + 1
                else:
                    num_pattern = len(s[i:]) - len(s[i:].lstrip(p[j])) + 1

                for k in range(num_pattern):
                    if self.isMatch(s[i + k:], p[j + 2:]):
                        return True

                return False
            else:
                if i < len(s) and self.char_match(s[i], p[j]):
                    i += 1
                    j += 1
                else:
                    return False

        if i == len(s) and j == len(p):
            return True
        else:
            return False

    def char_match(self, s, p):
        if p == '.':
            return True
        else:
            return s == p

if __name__ == "__main__":
    pass
