import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums,n = test_input
        nums = nums.copy()
        head = ListNode(nums.pop(0))
        last = head
        for num in nums:
            last.next = ListNode(num)
            last = last.next
        head = self.removeNthFromEnd(head,n)
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        last = back_pointer = front_pointer = head
        for i in range(n):
            front_pointer = front_pointer.next
        while front_pointer:
            front_pointer = front_pointer.next
            last = back_pointer
            back_pointer = back_pointer.next
        if last != back_pointer:
            last.next = back_pointer.next
        else:
            head = head.next
        return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
