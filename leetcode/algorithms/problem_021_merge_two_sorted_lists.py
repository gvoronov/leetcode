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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3_head = ListNode(None)
        l3 = l3_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                if l1 is not None:
                    l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                if l2 is not None:
                    l2 = l2.next

            l3 = l3.next

        if l1 is not None:
            l3.next = l1
        elif l2 is not None:
            l3.next = l2

        return l3_head.next

if __name__ == "__main__":
    print listnode_to_list(Solution().mergeTwoLists(list_to_listnode([]), list_to_listnode([])))
