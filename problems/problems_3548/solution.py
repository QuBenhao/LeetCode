import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canPartitionGrid(test_input)

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # Whether a horizontal split is possible
        def check(a: List[List[int]]) -> bool:
            m, n = len(a), len(a[0])

            # Whether removing one number from the upper part satisfies the requirements
            def f(a: List[List[int]]) -> bool:
                st = {0}  # 0 corresponds to removing no number
                s = 0
                for i, row in enumerate(a[:-1]):
                    for j, x in enumerate(row):
                        s += x
                        # In the first row, an interior element cannot be removed
                        if i > 0 or j == 0 or j == n - 1:
                            st.add(x)
                    # Handle the single-column case separately: only the first number or the number next to the split can be removed
                    if n == 1:
                        if s * 2 == total or s * 2 - total == a[0][0] or s * 2 - total == row[0]:
                            return True
                        continue
                    if s * 2 - total in st:
                        return True
                    # If the split is farther down, elements in the first row can be removed
                    if i == 0:
                        st.update(row)
                return False

            # Remove a number from the upper part or from the lower part
            return f(a) or f(a[::-1])

        # Horizontal split or vertical split
        return check(grid) or check(list(zip(*grid)))
