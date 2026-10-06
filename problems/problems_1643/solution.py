import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthSmallestPath(*test_input)

    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        # Arrange h identical 'H' characters and v identical 'V' characters
        # Choose h positions for 'H' in a sequence of length h+v
        # Thus, h and v give comb(h+v,h) combinations
        v, h = destination
        res = ''
        while h > 0 and v > 0:
            # Paths starting with 'H' precede those starting with 'V'; choosing 'H' reduces h by 1 and leaves v unchanged
            # Number of combinations with 'H' here
            num = math.comb(h + v - 1, h - 1)
            # If choosing 'H' gives fewer than k paths, choose V and find path k-num among the remaining paths
            if k > num:
                res += 'V'
                v -= 1
                k -= num
            # Otherwise, choose 'H' and continue deciding between 'H' and 'V'
            else:
                res += 'H'
                h -= 1
        # At a boundary, only one path remains: go straight to the destination
        return res + h * 'H' + v * 'V'
