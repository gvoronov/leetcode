import random

from leetcode.algorithms.problem_016_3sum_closest import Solution

def test_01():
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0

def test_02():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
