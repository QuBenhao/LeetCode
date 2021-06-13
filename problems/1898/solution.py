import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, p, removable = test_input
        return self.maximumRemovals(str(s), str(p), list(removable))

    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """

        def helper(k):
            nonlocal s, p
            l = []
            se = set(removable[:k])
            for i, c in enumerate(s):
                if i not in se:
                    l.append(c)
            return self.isSubsequence(p, ''.join(l))

        n = len(removable)
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left

    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n