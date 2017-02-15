from leetcode.algorithms.problem_015_3sum import Solution

def test_01():
    assert set([tuple(l) for l in Solution().threeSum([-1,0,1,2,-1,-4])]) == set([
        (-1, 0, 1), (-1, -1, 2)
    ])

def test_02():
    assert set([tuple(l) for l in Solution().threeSum([-1,0])]) == set([])

def test_03():
    assert set([tuple(l) for l in Solution().threeSum([])]) == set([])

def test_04():
    assert set([tuple(l) for l in Solution().threeSum([1,1,1])]) == set([])
