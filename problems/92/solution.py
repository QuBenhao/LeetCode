import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, m, n = test_input
        nums = nums.copy()
        head = curr = None
        while nums:
            val = nums.pop(0)
            if head:
                curr.next = ListNode(val)
                curr = curr.next
            else:
                head = curr = ListNode(val)
        ans = []
        curr = self.reverseBetween(head, m, n)
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            if n == 1:
                self.successor = head.next
                return head
            last = self.reverseBetween(head.next, m, n - 1)
            head.next.next = head
            head.next = self.successor
            return last

        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

        # temp = ListNode()
        # temp.next = head
        # head = temp
        #
        # index = 0
        # start = head
        # l = r = head.next
        #
        # while index < n - 1:
        #     if index < m - 1:
        #         start = r
        #     elif index == m - 1:
        #         l = r
        #     r = r.next
        #     index += 1
        #
        # while start.next != r:
        #     start.next = l.next
        #     l.next = r.next
        #     r.next = l
        #     l = start.next
        #
        # return head.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
