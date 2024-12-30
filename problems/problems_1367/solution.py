import solution
from typing import *
from python.object_libs import list_to_tree, list_to_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head, root = test_input
        return self.isSubPath(list_to_linked_list(head), list_to_tree(root))

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(h, r):
            if not h:
                return True
            if not r:
                return False
            return h.val == r.val and (dfs(h.next, r.left) or dfs(h.next, r.right)) or \
                   h is head and (dfs(head, r.left) or dfs(head, r.right))

        return dfs(head, root)
