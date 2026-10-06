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
        # Initialize with every node as a starting point
        frontier = [(i, 1 << i) for i in range(n)]
        explored = set(frontier)
        # The goal is 2^n - 1
        goal = (1 << n) - 1
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # Next state
                    successor = (other, 1 << other | state)
                    # The new state has not been visited
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # The graph is disconnected
        return -1
