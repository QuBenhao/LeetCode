import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = TodoList()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class TodoList:

    def __init__(self):
        pass


    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
                pass


    def getAllTasks(self, userId: int) -> List[str]:
            pass


    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
            pass


    def completeTask(self, userId: int, taskId: int) -> None:
            pass



# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)