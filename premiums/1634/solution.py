import solution
from typing import *


class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

# Definition for polynomial singly-linked list.

class Solution(solution.Solution):
    def solve(self, test_input=None):
        poly1, poly2 = test_input
        return self.addPoly(poly1, poly2)

    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
            pass
        
        