import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FileSharing(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class FileSharing:

    def __init__(self, m: int):
        pass


    def join(self, ownedChunks: List[int]) -> int:
            pass


    def leave(self, userID: int) -> None:
            pass


    def request(self, userID: int, chunkID: int) -> List[int]:
            pass



# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)