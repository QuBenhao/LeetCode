import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Graph(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
            pass


    def addEdge(self, edge: List[int]) -> None:
            pass


    def shortestPath(self, node1: int, node2: int) -> int:
            pass



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)