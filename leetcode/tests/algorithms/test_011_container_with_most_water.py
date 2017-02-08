from leetcode.algorithms.problem_011_container_with_most_water import Solution

def test_01():
    assert Solution().maxArea([1, 1]) == 1

def test_02():
    assert Solution().maxArea([1, 2]) == 1

def test_03():
    assert Solution().maxArea([1, 2, 3]) == 2
