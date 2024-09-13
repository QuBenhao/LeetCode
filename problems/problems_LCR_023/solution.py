import solution
from typing import *
from python.object_libs import list_to_linked_list, list_to_linked_list_intersection, linked_list_to_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        iv, nums1, nums2, idx1, idx2 = test_input
        head1, head2 = list_to_linked_list_intersection(iv, nums1, nums2, idx1, idx2)
        res = self.getIntersectionNode(head1, head2)
        return linked_list_to_list(res)

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a
