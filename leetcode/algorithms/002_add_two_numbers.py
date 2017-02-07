# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # print l1.val
        # print l1.next.val
        # self.print_ListNode(l1)
        # self.print_ListNode(l2)

        solution = ListNode(None)
        sum_node = solution

        len1 = self.length_ListNode(l1)
        len2 = self.length_ListNode(l2)

        if len1 >= len2:
            n1, n2 = l1, l2
        else:
            n1, n2 = l2, l1
            len1, len2 = len2, len1

        carry_over = 0
        for i in range(len2):
            digit_sum = n1.val + n2.val + carry_over
            n1, n2 = n1.next, n2.next

            if digit_sum >= 10:
                digit_sum = digit_sum - 10
                carry_over = 1
            else:
                carry_over = 0

            sum_node.next = ListNode(digit_sum)
            sum_node = sum_node.next

        for i in range(len1 - len2):
            digit_sum = n1.val + carry_over
            n1 = n1.next

            if digit_sum >= 10:
                digit_sum = digit_sum - 10
                carry_over = 1
            else:
                carry_over = 0

            sum_node.next = ListNode(digit_sum)
            sum_node = sum_node.next

        if carry_over == 1:
            sum_node.next = ListNode(1)
            sum_node = sum_node.next

        # self.print_ListNode(solution.next)
        return solution.next

    def print_ListNode(self, l):
        node = l
        ln_str = str(l.val)

        while node.next is not None:
            node = node.next
            ln_str += ' -> {}'.format(node.val)

        print ln_str

    def length_ListNode(self, l):
        node, counter = l, 0
        while node is not None:
            node = node.next
            counter += 1

        return counter

        
