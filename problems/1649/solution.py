import solution
from sortedcontainers import SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.createSortedArray(list(test_input))

    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        pq = SortedList([])
        ans = 0
        for i in instructions:
            ans = (ans + min(pq.bisect_left(i), len(pq) - pq.bisect_right(i))) % (10 ** 9 + 7)
            pq.add(i)
        return ans

        # m = max(instructions)
        # c = [0] * (m + 1)
        #
        # def update(x):
        #     while x <= m:
        #         c[x] += 1
        #         x += x & -x
        #
        # def get(x):
        #     r = 0
        #     while x > 0:
        #         r += c[x]
        #         x -= x & -x
        #     return r
        #
        # res = 0
        # for i, a in enumerate(instructions):
        #     res += min(get(a - 1), i - get(a))
        #     update(a)
        # return res % (10**9 + 7)
