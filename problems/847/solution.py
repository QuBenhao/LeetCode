import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestPathLength([x[:] for x in test_input])

    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        explored = set()
        frontier = [(i, 1 << i) for i in range(n)]
        goal = (1 << n) - 1
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                explored.add((cur, state))
                for other in graph[cur]:
                    successor = (other, 1 << other | state)
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # 图不连通
        return -1
