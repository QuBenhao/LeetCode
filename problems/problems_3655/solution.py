import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.xorAfterQueries(*test_input)

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # Total multiplier for each position
        mult = [1] * n

        # Process groups by k
        groups = defaultdict(list)  # k -> [(l, r, v), ...]
        for l, r, k, v in queries:
            groups[k].append((l, r, v))

        for k, ops in groups.items():
            # Difference array
            diff = defaultdict(lambda: 1)

            for l, r, v in ops:
                diff[l] = (diff[l] * v) % MOD
                next_pos = l + ((r - l) // k + 1) * k
                if next_pos < n:
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[next_pos] = (diff[next_pos] * inv_v) % MOD

            # Process difference points grouped by residue class
            # rem_diffs[rem] = [(pos, val), ...]
            rem_diffs = defaultdict(list)
            for pos, val in diff.items():
                rem_diffs[pos % k].append((pos, val))

            for rem, items in rem_diffs.items():
                items.sort()
                cur = 1
                idx = 0
                for pos in range(rem, n, k):
                    # Apply all differences at this position
                    while idx < len(items) and items[idx][0] == pos:
                        cur = (cur * items[idx][1]) % MOD
                        idx += 1
                    mult[pos] = (mult[pos] * cur) % MOD

        # Final result
        result = 0
        for i in range(n):
            val = (nums[i] * mult[i]) % MOD
            result ^= val
        return result

