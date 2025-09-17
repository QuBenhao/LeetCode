import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = TaskManager(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        pass

    def add(self, userId: int, taskId: int, priority: int) -> None:
        pass

    def edit(self, taskId: int, newPriority: int) -> None:
        pass

    def rmv(self, taskId: int) -> None:
        pass

    def execTop(self) -> int:
        pass

