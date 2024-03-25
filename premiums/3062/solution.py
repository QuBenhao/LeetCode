import solution
from typing import *
from object_libs import list_to_linked_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        return self.gameResult(heads)

    def gameResult(self, head: Optional[ListNode]) -> str:
            pass