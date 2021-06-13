import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        chalk, k = test_input
        return self.chalkReplacer(list(chalk), k)

    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(chalk)
        k %= s
        i = 0
        while k:
            if k < chalk[i]:
                return i
            k -= chalk[i]
            i += 1
        return i
