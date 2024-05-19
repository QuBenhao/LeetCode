import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumBoxes(test_input)

    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = i = j = 0
        while cur < n:
            j += 1
            i += j
            cur += i
        if cur == n:
            return i
        cur -= i
        i -= j
        j = 0
        while cur < n:
            j += 1
            cur += j
        return i + j
