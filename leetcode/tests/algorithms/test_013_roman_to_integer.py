from leetcode.algorithms.problem_013_roman_to_integer import Solution

def test_01():
    assert Solution().romanToInt("MMMCMXCIX") == 3999

def test_02():
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("II") == 2
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("V") == 5
    assert Solution().romanToInt("VI") == 6
    assert Solution().romanToInt("VII") == 7
    assert Solution().romanToInt("VIII") == 8
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("X") == 10

def test_03():
    assert Solution().romanToInt("CD") == 400
    assert Solution().romanToInt("CDXXXI") == 431
