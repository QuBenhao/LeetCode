import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, nums1 = test_input
        head1 = list_to_linked_list(nums1)
        res = self.modifiedList(nums, head1)
        return linked_list_to_list(res)

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
