import solution
from object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, n = test_input
        head = list_to_linked_list(nums)
        root = self.removeNthFromEnd(head, n)
        return linked_list_to_list(root)

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
