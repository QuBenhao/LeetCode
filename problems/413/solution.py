import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArithmeticSlices(list(test_input))

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        curr_d = None
        curr_len = 1
        for i in range(1, len(A)):
            if A[i] - A[i - 1] == curr_d:
                curr_len += 1
            else:
                if curr_len >= 2:
                    ans += (curr_len - 1) * curr_len // 2
                curr_len = 1
                curr_d = A[i] - A[i - 1]
        if curr_len >= 2:
            ans += (curr_len - 1) * curr_len // 2
        return ans
