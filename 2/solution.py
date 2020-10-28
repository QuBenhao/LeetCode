import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        l1_nums, l2_nums = test_input

        def construct_list(nums):
            p = head = ListNode(0)
            for i in nums:
                p.next = ListNode(i)
                p = p.next
            return head.next

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
        carry = 0
        pointer = root = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            if carry >= 10:
                s = carry - 10
                carry = 1
            else:
                s = carry
                carry = 0
            pointer.next = ListNode(s)
            pointer = pointer.next
        return root.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
