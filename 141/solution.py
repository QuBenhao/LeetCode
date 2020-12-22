import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, pos = test_input
        nums = nums.copy()
        index = 0
        curr = head = ListNode(nums.pop(0))
        node = None
        while nums:
            if index == pos:
                node = curr
            curr.next = ListNode(nums.pop(0))
            curr = curr.next
            index += 1
        if node:
            curr.next = node
        return self.hasCycle(head)

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
        return False


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
