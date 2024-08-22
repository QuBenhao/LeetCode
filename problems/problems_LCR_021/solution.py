import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, n = test_input
        head0 = list_to_linked_list(nums0)
        res = self.removeNthFromEnd(head0, n)
        return linked_list_to_list(res)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass

