import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findCircleNum([x[:] for x in test_input])

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(city):
            not_explored.remove(city)
            for i in range(n):
                if i == city or i not in not_explored:
                    continue
                if isConnected[city][i]:
                    dfs(i)

        n = len(isConnected)
        not_explored = [i for i in range(n)]
        count = 0
        while not_explored:
            dfs(not_explored[0])
            count += 1
        return count
