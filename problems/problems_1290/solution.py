import solution
from python.object_libs import list_to_linked_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_list(test_input)
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
