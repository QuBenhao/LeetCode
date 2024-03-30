import solution
from typing import *
from object_libs import list_to_linked_list, linked_list_to_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, a, b, nums3 = test_input
        head0 = list_to_linked_list(nums0)
        head3 = list_to_linked_list(nums3)
        res = self.mergeInBetween(head0, a, b, head3)
        return linked_list_to_list(res)

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if a == list1.val:
            root = list2
        else:
            root = list1
        l1 = list1
        node = list2
        count = 1
        while count < a:
            l1 = l1.next
            count += 1
        r1 = l1
        while count <= b:
            r1 = r1.next
            count += 1
        r1 = r1.next
        while node.next is not None:
            node = node.next
        l1.next = list2
        node.next = r1
        return root
