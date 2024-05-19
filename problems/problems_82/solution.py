import solution
from python.object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_list(test_input)
        root = self.deleteDuplicates(head)
        return linked_list_to_list(root)

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
