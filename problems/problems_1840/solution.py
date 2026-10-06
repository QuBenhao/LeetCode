import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxBuilding(*test_input)

    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.extend([[1, 0], [n, n - 1]])
        restrictions.sort()
        m = len(restrictions)
        # The key is making every restriction valid and effective
        # Height limit at the right boundary
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])
        # Height limit at the left boundary
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])

        ans = 0
        for i in range(1, m):
            l, limit_l = restrictions[i - 1]
            r, limit_r = restrictions[i]
            # Derive the maximum height from the left and right limits
            # We have h_max - limit_l <= max_idx - l and h_max - limit_r <= r - max_idx
            # Adding them gives h_max <= (r - l + limit_r + limit_l) // 2
            ans = max(ans, (r + limit_l + limit_r - l) // 2)
        return ans
