from leetcode.algorithms.problem_026_remove_duplicates_from_sorted_array import Solution

def test_01():
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2
    assert nums == [1, 2]


def test_02():
    nums = [0]
    assert Solution().removeDuplicates(nums) == 1
    assert nums == [0]

def test_03():
    nums = []
    assert Solution().removeDuplicates(nums) == 0
    assert nums == []

def test_04():
    nums = [0, 1, 2, 3]
    assert Solution().removeDuplicates(nums) == 4
    assert nums == [0, 1, 2, 3]
