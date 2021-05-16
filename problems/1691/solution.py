import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxHeight(test_input.copy())

    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        # cuboids = cuboids.copy()
        for cuboid in cuboids:
            cuboid.sort(reverse=True)

        cuboids.sort(key=lambda x: [-x[0],-x[1],-x[2]])

        dp = [cuboids[i][0] for i in range(len(cuboids))]

        for i in range(1, len(cuboids)):
            for j in range(i):
                if cuboids[j][0] >= cuboids[i][0] and cuboids[j][1] >= cuboids[i][1] and cuboids[j][2] >= cuboids[i][2]:
                    dp[i] = max(dp[j] + cuboids[i][0], dp[i])

        return max(dp)
