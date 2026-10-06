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
            k += 1  # Binary-search for the smallest infeasible k+1; the final k is the largest feasible count
            # Greedy: use the k strongest workers to complete the k easiest tasks
            i, p = 0, pills
            valid_tasks = deque()
            for w in workers[-k:]:  # Iterate over workers
                # Record tasks the worker can complete with a pill in valid_tasks
                while i < k and tasks[i] <= w + strength:
                    valid_tasks.append(tasks[i])
                    i += 1
                # Cannot complete any task even with a pill
                if not valid_tasks:
                    return True
                # Can complete the easiest task without a pill
                if w >= valid_tasks[0]:
                    valid_tasks.popleft()
                    continue
                # A pill is required
                if p == 0:  # No pills remain
                    return True
                p -= 1
                # Complete the hardest feasible task
                valid_tasks.pop()
            return False

        return bisect_left(range(min(len(tasks), len(workers))), True, key=check)
