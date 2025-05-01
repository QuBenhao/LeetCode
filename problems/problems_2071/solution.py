from bisect import bisect_left
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTaskAssign(*test_input)

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            k += 1  # 二分最小的无法完成的 k+1，那么最终的 k 就是最大的可以完成的 k
            # 贪心：用最强的 k 名工人，完成最简单的 k 个任务
            i, p = 0, pills
            valid_tasks = deque()
            for w in workers[-k:]:  # 枚举工人
                # 在吃药的情况下，把能完成的任务记录到 valid_tasks 中
                while i < k and tasks[i] <= w + strength:
                    valid_tasks.append(tasks[i])
                    i += 1
                # 即使吃药也无法完成任务
                if not valid_tasks:
                    return True
                # 无需吃药就能完成（最简单的）任务
                if w >= valid_tasks[0]:
                    valid_tasks.popleft()
                    continue
                # 必须吃药
                if p == 0:  # 没药了
                    return True
                p -= 1
                # 完成（能完成的）最难的任务
                valid_tasks.pop()
            return False

        return bisect_left(range(min(len(tasks), len(workers))), True, key=check)
