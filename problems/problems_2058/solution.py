import solution
from typing import *
from python.object_libs import list_to_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        return self.nodesBetweenCriticalPoints(head0)

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pass

