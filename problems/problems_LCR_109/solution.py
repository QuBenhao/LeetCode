import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.openLock(*test_input)

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        visited = {"0000"}
        queue = deque(["0000"])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for i in range(4):
                    for j in [-1, 1]:
                        new_node = node[:i] + str((int(node[i]) + j) % 10) + node[i + 1:]
                        if new_node == target:
                            return step
                        if new_node not in deadends and new_node not in visited:
                            visited.add(new_node)
                            queue.append(new_node)
        return -1
