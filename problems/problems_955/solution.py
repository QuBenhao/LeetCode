import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDeletionSize(test_input)

    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        check_list = list(range(n - 1))

        ans = 0
        for j in range(m):
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    # Column j is not in ascending order and must be deleted
                    ans += 1
                    break
            else:
                # Column j is in ascending order, so keeping it is better
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        # Adjacent letters are equal; continue comparing rows i and i+1 in the next column
                        check_list[new_size] = i  # Overwrite in place
                        new_size += 1
                del check_list[new_size:]
        return ans
