import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        res = self.mergeKLists(heads)
        return linked_list_to_list(res)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

