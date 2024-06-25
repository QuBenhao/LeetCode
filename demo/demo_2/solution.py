import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, nums1 = test_input
        head0 = list_to_linked_list(nums0)
        head1 = list_to_linked_list(nums1)
        res = self.addTwoNumbers(head0, head1)
        return linked_list_to_list(res)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass

