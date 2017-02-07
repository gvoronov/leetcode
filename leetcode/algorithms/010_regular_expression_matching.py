class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if p == '.*' or s == p:
            return True

        i, j = 0, 0
        while i < len(s) and j < len(p):
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
                if self.char_match(s[i], p[j]):
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

def test_01():
    assert Solution().isMatch("aa","a") == False

def test_02():
    assert Solution().isMatch("aa","aa") == True

def test_03():
    assert Solution().isMatch("aaa","aa") == False

def test_04():
    assert Solution().isMatch("aa", "a*") == True

def test_05():
    assert Solution().isMatch("aa", ".*") == True

def test_06():
    assert Solution().isMatch("ab", ".*") == True

def test_07():
    assert Solution().isMatch("aab", "c*a*b") == True

def test_08():
    assert Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b") == True

def test_09():
    assert Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False

def test_10():
    assert Solution().isMatch("aaaaaaaaaaaaab", ".*") == True

def test_11():
    assert Solution().isMatch("", ".*") == True

def test_12():
    assert Solution().isMatch("asdfa", ".*a") == True

def test_13():
    assert Solution().isMatch("asdfab", ".*a") == False

def test_14():
    assert Solution().isMatch("aaa", "a.a") == True

def test_14():
    assert Solution().isMatch("a", "ab*") == True

if __name__ == "__main__":
    print Solution().isMatch("aaa", "a.a")
