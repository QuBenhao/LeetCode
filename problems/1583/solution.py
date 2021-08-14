import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, preferences, pairs = test_input
        return self.unhappyFriends(n, [x[:] for x in preferences], [x[:] for x in pairs])

    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        """
        之前男生x和女生u是一对，轰轰烈烈的爱了一场，但是迫于生活和现实，分手走散了。
        若干年后，x在前女友u的婚礼上，男生x发现，自己迫于无奈找了一个不太爱的人y；
        而前女友u也找了一个不太爱的人v。男生x酒后痛哭，觉得非常难过，我们最终还是败给了现实。
        """
        mark = [[0] * n for _ in range(n)]
        for i, pref in enumerate(preferences):
            for j, lover in enumerate(pref):
                mark[i][lover] = j

        couple = dict()
        for a,b in pairs:
            couple[a] = b
            couple[b] = a

        ans = 0
        for x in range(n):
            y = couple[x]
            for u in range(n):
                if u == x or u == y:
                    continue
                v = couple[u]
                if mark[x][y] > mark[x][u] and mark[u][v] > mark[u][x]:
                    ans += 1
                    break
        return ans
