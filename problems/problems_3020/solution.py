import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumLength(test_input)

    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1  # At least one element can be selected

        # Handle x=1 separately: since 1^2 = 1, it forms a sequence of all ones
        # The sequence length must be odd (one peak, with the rest symmetric)
        if 1 in count:
            c = count[1]
            max_len = max(max_len, c if c % 2 == 1 else c - 1)

        for x in count:
            if x == 1:
                continue
            # A sequence of length > 1 requires count[x] >= 2
            if count[x] < 2:
                continue

            # Build a chain: each number is the square of the previous one and is present in the array
            chain = [x]
            while chain[-1] ** 2 in count:
                chain.append(chain[-1] ** 2)

            # Find the first position with count < 2 to use as the peak
            # By default, the peak is the last number in the chain
            peak_idx = len(chain) - 1
            for i, val in enumerate(chain):
                if count[val] < 2:
                    # A number with count >= 1 can be the peak; if count == 0, use the previous number
                    peak_idx = i if count[val] >= 1 else i - 1
                    break

            if peak_idx >= 0:
                max_len = max(max_len, 2 * peak_idx + 1)

        return max_len

