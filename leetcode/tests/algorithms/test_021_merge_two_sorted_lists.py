from leetcode.algorithms.problem_021_merge_two_sorted_lists import Solution
from leetcode.algorithms.problem_021_merge_two_sorted_lists import listnode_to_list
from leetcode.algorithms.problem_021_merge_two_sorted_lists import list_to_listnode

def test_01():
    assert listnode_to_list(Solution().mergeTwoLists(list_to_listnode([]), list_to_listnode([]))) == []


def test_02():
    assert listnode_to_list(Solution().mergeTwoLists(list_to_listnode([1, 2]), list_to_listnode([2, 3]))) == [1, 2, 2, 3]
