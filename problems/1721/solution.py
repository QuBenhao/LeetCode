import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
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
        curr = self.swapNodes(head, k)
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1,head)
        firstPrev = dummy
        for i in range(k-1):
            firstPrev = firstPrev.next

        secondPrev = dummy
        advanced = firstPrev.next.next
        while advanced:
            secondPrev = secondPrev.next
            advanced = advanced.next

        first = firstPrev.next
        second = secondPrev.next
        firstNodeAfter = first.next
        secondNodeAfter = second.next
        if second.next == first:
            secondPrev.next = first
            first.next = second
            second.next = firstNodeAfter
        elif secondPrev == first:
            firstPrev.next = second
            second.next = first
            first.next = secondNodeAfter
        else:
            firstPrev.next = second
            second.next = firstNodeAfter
            secondPrev.next = first
            first.next = secondNodeAfter
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
