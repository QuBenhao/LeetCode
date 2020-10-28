import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        l1_nums, l2_nums = test_input

        def construct_list(nums):
            nodes = []
            for i in nums:
                nodes.append(ListNode(val=i, next=None))
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            return nodes[0]

        l1 = construct_list(l1_nums)
        l2 = construct_list(l2_nums)
        root = self.addTwoNumbers(l1, l2)
        l = []
        while root:
            l.append(root.val)
            root = root.next
        return l

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer1 = l1
        pointer2 = l2
        carry = 0
        root = ListNode(val=0, next=None)
        pointer = root
        while pointer1 or pointer2 or carry:
            if pointer1:
                carry += pointer1.val
                pointer1 = pointer1.next
            if pointer2:
                carry += pointer2.val
                pointer2 = pointer2.next
            if carry >= 10:
                s = carry % 10
                carry = 1
            else:
                s = carry
                carry = 0
            pointer.next = ListNode(s, next=None)
            pointer = pointer.next
        return root.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
