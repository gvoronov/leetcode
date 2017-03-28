from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import Solution
from leetcode.algorithms.problem_019_remove_nth_node_from_end_of_list import ListNode

def list_to_listnode(l):
    l_it = iter(l)

    linked_list = ListNode(l_it.next())
    for val in l:
        linked_list.next = ListNode(val)

    return linked_list


def listnode_to_list(ln):
    l = list()
    node = ln
    while node is not None:
        l.append(node.val)
        node = node.next

    return l

def test_01():
    pass

if __name__ == "__main__":
    # print list_to_listnode([1, 2, 3, 4, 5]).val
    print listnode_to_list(list_to_listnode([1, 2, 3, 4, 5]))
