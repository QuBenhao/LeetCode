import solution
from python.object_libs import list_to_linked_list_intersection


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        res = self.getIntersectionNode(*list_to_linked_list_intersection(*test_input))
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
