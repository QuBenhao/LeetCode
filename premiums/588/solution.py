import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FileSystem()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class FileSystem:

    def __init__(self):
        pass


    def ls(self, path: str) -> List[str]:
            pass


    def mkdir(self, path: str) -> None:
            pass


    def addContentToFile(self, filePath: str, content: str) -> None:
            pass


    def readContentFromFile(self, filePath: str) -> str:
            pass



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)