import solution
from python.object_libs import list_to_linked_list, linked_list_to_list
from typing import *



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        vals, target = test_input
        node = list_to_linked_list(vals)
        tmp = node
        idx = vals.index(target)
        for _ in range(idx):
            tmp = tmp.next
        self.deleteNode(tmp)
        return linked_list_to_list(node)

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
