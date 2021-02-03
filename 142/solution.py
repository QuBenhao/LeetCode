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
        start = self.detectCycle(head)
        if start:
            return start.val
        return start

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None

            # slow == ENTRY, fast == HEAD -> ENTRY * 2
            # slow == fast:
            # t % C == 2 * t + HEAD -> ENTRY % C
            # t % C == - HEAD -> ENTRY
            if fast == slow:
                break

        if not fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
