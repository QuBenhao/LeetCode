import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decode(list(test_input))

    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        # perm[0] ^ perm[1] = encoded[0]
        # perm[0] ^ perm[2] = encoded[0] ^ encoded[1]
        # perm[0] ^ perm[3] = encoded[0] ^ encoded[1] ^ encoded[2]
        # perm[0] ^ perm[n-1] = encoded[0] ^ encoded[1] ^ .. ^ encoded[n-2]
        # Optimization: encoded[0] occurs n-1 times (even), encoded[1] occurs n-2 times (odd), and so on
        start = 0
        for i in range(1, n, 2):
            start ^= encoded[i]
        if n % 4 == 1:
            start ^= 1
        perm = [start]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
