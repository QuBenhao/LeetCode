import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wonderfulSubstrings(str(test_input))

    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # At position i, encode the parity of counts for a through j in prefix 0..i using 10 bits: 0 for even, 1 for odd
        # Bitmask of count parities from 0 through i
        ans = mask = 0
        # Count each bitmask seen so far; the empty prefix occurs once
        freq = defaultdict(int, {0:1})
        for c in word:
            u = ord(c) - ord('a')
            # Toggle the current character's count parity
            mask ^= 1 << u
            for i in range(10):
                # Count masks differing only in bit i: the intervening substring has an odd count for character i
                ans += freq[mask ^ 1 << i]
            # Count substrings where every character appears an even number of times
            ans += freq[mask]
            freq[mask] += 1
        return ans
