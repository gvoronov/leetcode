def list_to_listnode(l):
    if len(l) == 0:
        return None

    l_it = iter(l)

    head_node = ListNode(l_it.next())
    node = head_node

    for val in l_it:
        node.next = ListNode(val)
        node = node.next

    return head_node


def listnode_to_list(ln):
    l = list()
    node = ln
    while node is not None:
        l.append(node.val)
        node = node.next

    return l

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        tail_start_node = head
        tail_end_node = head
        for i in range(n):
            tail_end_node = tail_end_node.next

        if tail_end_node is None:
            return head.next

        while tail_end_node.next is not None:
            tail_start_node = tail_start_node.next
            tail_end_node = tail_end_node.next

        tail_start_node.next = tail_start_node.next.next

        return head


if __name__ == "__main__":
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 1))
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 2))
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 3))
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 4))
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1, 2, 3, 4, 5]), 5))
    print listnode_to_list(Solution().removeNthFromEnd(list_to_listnode([1]), 1))
