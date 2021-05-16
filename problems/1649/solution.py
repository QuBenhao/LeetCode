import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.createSortedArray(list(test_input))

    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while x <= m:
                c[x] += 1
                x += x & -x

        def get(x):
            r = 0
            while x > 0:
                r += c[x]
                x -= x & -x
            return r

        res = 0
        for i, a in enumerate(instructions):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)
