import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        curr = head = ListNode(test_input.pop(0))
        while test_input:
            curr.next = ListNode(test_input.pop(0))
            curr = curr.next
        return self.getDecimalValue(head)

    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        sum = 0
        while head:
            sum *= 2
            sum += head.val
            head = head.next
        return sum


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def setNext(self, next):
        self.next = next
