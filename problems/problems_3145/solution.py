import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findProductsOfElements(test_input)

    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def sum_e(k: int) -> int:
            res = n = cnt1 = sum_i = 0
            for i in range((k + 1).bit_length() - 1, 0, -1):
                c = (cnt1 << i) + (i << (i - 1))  # Number of additional exponents
                if c <= k:
                    k -= c
                    res += (sum_i << i) + ((i * (i - 1) // 2) << (i - 1))
                    sum_i += i  # Sum of exponents for the ones already placed
                    cnt1 += 1  # Number of ones already placed
                    n |= 1 << i  # Place a 1
            # Handle the lowest bit separately
            if cnt1 <= k:
                k -= cnt1
                res += sum_i
                n |= 1  # Set the lowest bit to 1
            # Supply the remaining k exponents from the k lowest set bits of n
            for _ in range(k):
                lb = n & -n
                res += lb.bit_length() - 1
                n ^= lb  # Clear the lowest set bit (set it to 0)
            return res

        return [pow(2, sum_e(r + 1) - sum_e(l), mod) for l, r, mod in queries]
