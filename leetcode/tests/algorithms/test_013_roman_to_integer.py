from leetcode.algorithms.problem_013_roman_to_integer import Solution

def test_01():
    assert Solution().intToRoman(3999) == "MMMCMXCIX"

def test_02():
    assert Solution().intToRoman(1) == "I"
    assert Solution().intToRoman(2) == "II"
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(5) == "V"
    assert Solution().intToRoman(6) == "VI"
    assert Solution().intToRoman(7) == "VII"
    assert Solution().intToRoman(8) == "VIII"
    assert Solution().intToRoman(9) == "IX"
    assert Solution().intToRoman(10) == "X"

def test_03():
    assert Solution().intToRoman(400) == "CD"
    assert Solution().intToRoman(431) == "CDXXXI"
