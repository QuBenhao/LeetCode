import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.splitPainting([x[:] for x in test_input])

    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        diff = defaultdict(int)
        points = set()
        right = 0
        for a, b, c in segments:
            diff[a] += c
            diff[b] -= c
            right = max(right, b)
            points.add(a)
            points.add(b)
        ans = []
        curr = 0
        left = None
        color = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if color and curr != color:
                if color and left is not None:
                    ans.append([left, i, color])
                if curr:
                    left = i
                    color = curr
                else:
                    left = None
            elif color and curr == color:
                if i in points and left is not None:
                    ans.append([left, i, color])
                    left = i
            if curr and left is None:
                left = i
                color = curr
        return ans
