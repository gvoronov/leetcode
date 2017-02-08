from leetcode.algorithms.problem_010_regular_expression_matching import Solution

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

def test_15():
    assert Solution().isMatch("", "c*c*") == True
