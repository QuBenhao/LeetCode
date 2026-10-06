import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValidSerialization(test_input)

    def isValidSerialization(self, preorder: str) -> bool:
        # splits = preorder.split(",")
        # stack = []
        # for node in splits:
        #     stack.append(node)
        #     while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
        #         for _ in range(3):
        #             stack.pop()
        #         stack.append("#")
        # return len(stack) == 1 and stack[0] == "#"

        # The tree initially has one slot; every entry consumes a slot, and a number creates two more slots (eventually filled by #)
        # Check whether slots run out too early or are exactly filled at the end
        total = 1
        for node in preorder.split(","):
            total -= 1
            if total < 0:
                return False
            if node != "#":
                total += 2
        return total == 0
