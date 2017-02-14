from leetcode.algorithms.problem_015_3sum import Solution

def test_01():
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [
        [-1, 0, 1], [-1, -1, 2]
    ]
