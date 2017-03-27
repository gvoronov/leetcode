import random

from leetcode.algorithms.problem_017_letter_combinations_of_a_phone_number import Solution

def test_01():
    assert set(Solution().letterCombinations('23')) == set(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

def test_02():
    assert set(Solution().letterCombinations('')) == set([])
