import solution
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_list(test_input)
        root = self.swapPairs(head)
        return linked_list_to_list(root)

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        back = ListNode()
        back.next = head
        front = head.next
        head = back
        while front:
            back.next.next = front.next
            front.next = back.next
            back.next = front
            back = front.next
            front = back.next
            if not front:
                break
            front = front.next
        return head.next
