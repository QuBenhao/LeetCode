import solution
from typing import *
from object_libs import call_method, list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        pass

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
            pass
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
            pass
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))