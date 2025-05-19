import solution
from typing import *



# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = test_input
        return self.flatten(head)

    def flatten(self, head: 'Node') -> 'Node':
        pass

