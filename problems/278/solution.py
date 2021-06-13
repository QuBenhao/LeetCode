import solution

BAD = 1


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, bad = test_input
        global BAD
        BAD = bad
        return self.firstBadVersion(n)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= BAD
