import solution
from object_libs import list_to_linked_list_intersection


class Solution(solution.Solution):
    def solve(self, test_input=None):
        intersect_val, list_a, list_b, skip_a, skip_b = test_input
        res = self.getIntersectionNode(*list_to_linked_list_intersection(intersect_val, list_a, skip_a, list_b, skip_b))
        return res.val if res else None

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        n1, n2 = headA, headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
