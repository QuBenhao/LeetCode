import solution
from typing import *



# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(solution.Solution):
    def solve(self, test_input=None):
        head, insertVal = test_input
        return self.insert(head, insertVal)

    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
            pass
        