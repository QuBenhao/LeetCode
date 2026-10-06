import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSubmatrixSumTarget(*test_input)

    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        # Same approach as 363, with space-optimized prefix sums; binary search is unnecessary here
        m, n = len(matrix), len(matrix[0])
        ans = 0
        # Fix the left column
        for i in range(1, n + 1):
            presum = [0] * (m + 1)
            # Fix the right column
            for j in range(i, n + 1):
                a = 0
                d = {0:1}
                # Select rows
                for fixed in range(1, m + 1):
                    # Prefix sum
                    presum[fixed] += matrix[fixed-1][j-1]
                    a += presum[fixed]
                    # Use a dictionary to count how many sums equal target
                    if a - target in d:
                        ans += d[a - target]
                    if a in d:
                        d[a] += 1
                    else:
                        d[a] = 1
        return ans
