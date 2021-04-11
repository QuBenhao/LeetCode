import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSideJumps(list(test_input))

    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        # 贪心
        n = len(obstacles)
        curr = 2
        lines = {1, 2, 3}
        ans = 0
        for i in range(n-1):
            # an obstacle in front of
            if obstacles[i+1] == curr:
                # places can jump to
                new_lines = lines - {curr, obstacles[i]}
                if len(new_lines) == 1:
                    curr = new_lines.pop()
                else:
                    # jump to the place where we can go as far as we can
                    max_index = -1
                    for j in new_lines:
                        try:
                            index = list.index(obstacles, j,i+1,n)
                            if index > max_index:
                                max_index = index
                                curr = j
                        except:
                            curr = j
                            return ans + 1
                ans += 1
        return ans

        # 动态规划
        # n = len(obstacles)
        # ans = [1, 0, 1]
        # for i in range(1,n-1):
        #     new = [float("inf")] * 3
        #     for j in range(3):
        #         for k in range(3):
        #             if j == obstacles[i-1] - 1 and k == obstacles[i] - 1:
        #                 new[j] = min(ans[k] + 2, new[j])
        #             elif j == obstacles[i - 1] - 1:
        #                 new[j] = min(ans[k] + 1, new[j])
        #             elif k != obstacles[i] - 1 and j == k:
        #                 new[j] = min(ans[j], new[j])
        #     ans = new
        # return min(ans)
