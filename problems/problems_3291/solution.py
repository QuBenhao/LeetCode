from random import randint

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minValidStrings(*test_input)

    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # Polynomial string hashing (for efficient substring hash computation)
        # Hash function hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # Randomize BASE to guard against adversarial inputs
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # Prefix hash pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # Compute the polynomial hash with Horner's method

        # Compute the hash of substring target[l:r]; this is the half-open interval [l,r)
        # The calculation is similar to prefix sums
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

        # Store the hash of every prefix of each words[i], grouped by length
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        for w in words:
            h = 0
            for j, b in enumerate(w):
                h = (h * BASE + ord(b)) % MOD
                sets[j].add(h)  # j starts at 0

        ans = 0
        cur_r = 0  # Right endpoint of the bridge already built
        nxt_r = 0  # Maximum right endpoint of the next bridge
        for i in range(n):
            while nxt_r < n and nxt_r - i < max_len and sub_hash(i, nxt_r + 1) in sets[nxt_r - i]:
                nxt_r += 1  # Extend as far as possible
            if i == cur_r:  # Reached the right endpoint of the bridge already built
                if i == nxt_r:  # No bridge can reach from i to i+1
                    return -1
                cur_r = nxt_r  # Build the next bridge
                ans += 1
        return ans
