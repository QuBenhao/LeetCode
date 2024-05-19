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
            return None
        front = head.next
        while front and front.val == head.val:
            front = front.next
        head.next = self.deleteDuplicates(front)
        return head

        # curr = head
        # while curr:
        #     node = curr.next
        #     while node and node.val == curr.val:
        #         curr.next = node.next
        #         node = node.next
        #     curr = curr.next
        # return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
