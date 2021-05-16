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
        ans = []
        while root:
            ans.append(root.val)
            root = root.next
        return ans

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = n2 = 0
        curr = l1
        while curr.next:
            n1 += curr.val
            n1 *= 10
            curr = curr.next
        n1 += curr.val
        if n1 == 0:
            return l2
        curr = l2
        while curr.next:
            n2 += curr.val
            n2 *= 10
            curr = curr.next
        n2 += curr.val
        if n2 == 0:
            return l1
        n = n1 + n2
        curr = last = None
        while n > 0:
            curr = ListNode(n % 10, last)
            last = curr
            n //= 10
        return curr


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
