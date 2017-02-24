import random

from leetcode.algorithms.problem_015_3sum import Solution

def make_comp(sol):
    set([tuple(sorted(l)) for l in sol])

def test_01():
    assert make_comp(Solution().threeSum([-1,0,1,2,-1,-4])) == make_comp([
        [-1, 0, 1], [-1, -1, 2]
    ])

def test_02():
    assert make_comp(Solution().threeSum([-1,0])) == make_comp([])

def test_03():
    assert make_comp(Solution().threeSum([])) == make_comp([])

def test_04():
    assert make_comp(Solution().threeSum([1,1,1])) == make_comp([])

def test_05():
    nums = [random.randint(-1000, 1000) for _ in range(100)]
    assert (make_comp(Solution().threeSum(nums)) ==
        make_comp(Solution().threeSum_slow_for_testing(nums)))

def test_06():
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    assert (make_comp(Solution().threeSum(nums)) ==
        make_comp(Solution().threeSum_slow_for_testing(nums)))

# def test_01():
#     assert set([tuple(l) for l in Solution().threeSum([-1,0,1,2,-1,-4])]) == set([
#         (-1, 0, 1), (-1, -1, 2)
#     ])
#
# def test_02():
#     assert set([tuple(l) for l in Solution().threeSum([-1,0])]) == set([])
#
# def test_03():
#     assert set([tuple(l) for l in Solution().threeSum([])]) == set([])
#
# def test_04():
#     assert set([tuple(l) for l in Solution().threeSum([1,1,1])]) == set([])
