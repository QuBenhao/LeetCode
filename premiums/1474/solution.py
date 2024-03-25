import solution
from typing import *
from object_libs import list_to_linked_list, linked_list_to_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr, m, n = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        res = self.deleteNodes(heads, m, n)
        return linked_list_to_list(res)

    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
                pass
        