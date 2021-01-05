import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        last = None
        for i in range(len(test_input) - 1, -1, -1):
            last = ListNode(test_input[i], next=last)
        head = self.deleteDuplicates(head=last)
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        curr = head
        front = head.next
        if front and front.val == curr.val:
            while front and front.val == curr.val:
                front = front.next
            return self.deleteDuplicates(front)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
