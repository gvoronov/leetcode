from leetcode.algorithms.problem_014_longest_common_prefix import Solution

def test_01():
    assert Solution().longestCommonPrefix([]) == ''

def test_02():
    assert Solution().longestCommonPrefix(['asdf', 'asdf12', 'asdfqwer']) == 'asdf'

def test_03():
    assert Solution().longestCommonPrefix(['asdf', '1asdf12', 'aasdfqwer']) == ''

def test_04():
    assert Solution().longestCommonPrefix(['aca', 'cba']) == ''
