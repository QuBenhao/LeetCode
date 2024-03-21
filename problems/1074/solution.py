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
        # 方法同363，空间优化前缀和。注:不使用二分最大效益因为用不到二分
        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 固定左边列
        for i in range(1, n + 1):
            presum = [0] * (m + 1)
            # 固定右边列
            for j in range(i, n + 1):
                a = 0
                d = {0:1}
                # 选择行
                for fixed in range(1, m + 1):
                    # 前缀和
                    presum[fixed] += matrix[fixed-1][j-1]
                    a += presum[fixed]
                    # 使用字典统计构成target有多少个
                    if a - target in d:
                        ans += d[a - target]
                    if a in d:
                        d[a] += 1
                    else:
                        d[a] = 1
        return ans
