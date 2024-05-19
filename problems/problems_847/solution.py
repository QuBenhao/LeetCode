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
        # 初始以每个点为起点
        frontier = [(i, 1 << i) for i in range(n)]
        explored = set(frontier)
        # 目标为2^n - 1
        goal = (1 << n) - 1
        step = 0
        while frontier:
            nxt = []
            for cur, state in frontier:
                if state == goal:
                    return step
                for other in graph[cur]:
                    # 下一个状态
                    successor = (other, 1 << other | state)
                    # 新的状态没有被走过
                    if successor not in explored:
                        explored.add(successor)
                        nxt.append(successor)
            frontier = nxt
            step += 1
        # 图不连通
        return -1
