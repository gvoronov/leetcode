from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import Solution
from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import ListNode
from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import list_to_listnode
from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import listnode_to_list

def test_01():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4]

def test_02():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]

def test_03():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 3)) == [1, 2, 4, 5]

def test_04():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 4)) == [1, 3, 4, 5]

def test_05():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 5)) == [2, 3, 4, 5]

def test_06():
    assert listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1]), 1)) == []

if __name__ == "__main__":
    # print list_to_listnode([1, 2, 3, 4, 5]).val
    print listnode_to_list(list_to_listnode([1, 2, 3, 4, 5]))
    print listnode_to_list(list_to_listnode([1]))
    print listnode_to_list(list_to_listnode([1, 3, 5]))
    print listnode_to_list(list_to_listnode([]))
