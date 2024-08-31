import solution
from typing import *
from python.object_libs import list_to_linked_list, list_to_linked_list_cycle, linked_list_to_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, pos0 = test_input
        head0 = list_to_linked_list_cycle(nums0, pos0)
        res = self.detectCycle(head0)
        return linked_list_to_list(res)

    def detectCycle(self, head: ListNode) -> ListNode:
        pass

