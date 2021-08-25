import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.allPathsSourceTarget([x[:] for x in test_input])

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        path = [0]
        ans = []

        def backtracking():
            if path[-1] == n - 1:
                ans.append(list(path))
            else:
                for nxt in graph[path[-1]]:
                    path.append(nxt)
                    backtracking()
                    path.pop()

        backtracking()
        return ans
