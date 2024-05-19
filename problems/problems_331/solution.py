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

        # 初始树只有一个槽位，每次填入东西都会减少一个槽位，填入数字会额外增加两个槽位(等待填#)
        # 看过程中是否槽位已满或最终是否刚好填满
        total = 1
        for node in preorder.split(","):
            total -= 1
            if total < 0:
                return False
            if node != "#":
                total += 2
        return total == 0
