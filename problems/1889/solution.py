import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        packages, boxes = test_input
        return self.minWastedSpace(list(packages), [x[:] for x in boxes])

    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        packages.sort()
        ans = float("inf")
        for box in boxes:
            box.sort()
            if packages[-1] > box[-1]:
                continue
            idx = 0
            curr = 0
            for b in box:
                last = idx
                idx = bisect.bisect_right(packages, b, lo=last)
                # 我们需要(idx-last)个箱子b
                curr += (idx - last) * b
            ans = min(ans, curr)
        return (ans-sum(packages)) % (10 ** 9 + 7) if ans != float("inf") else -1
