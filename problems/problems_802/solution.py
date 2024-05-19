import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.eventualSafeNodes([x[:] for x in test_input])

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # n = len(graph)
        # out = [0] * n
        # edges = defaultdict(list)
        # for i, nodes in enumerate(graph):
        #     for node in nodes:
        #         edges[node].append(i)
        #         # 统计所有点的出度
        #         out[i] += 1
        # q = deque([])
        # for i in range(n):
        #     if not out[i]:
        #         # 出度为0的点加入队列
        #         q.append(i)
        # while q:
        #     node = q.popleft()
        #     for front in edges[node]:
        #         # 去掉front->node这条边
        #         out[front] -= 1
        #         if not out[front]:
        #             # 如果去掉该边后front的出度变为0，加入队列
        #             q.append(front)
        # return [i for i in range(n) if not out[i]]

        n = len(graph)
        # 每个点可能的状态: -1:点是未走过的, 0:点是安全的，1:点是走过的不确定安不安全，2:点是不安全的
        states = [-1] * n

        def dfs(node):
            # 还未访问过
            if states[node] == -1:
                # 标记为状态1
                states[node] = 1
                for nxt in graph[node]:
                    states[node] += dfs(nxt)
                    # 已经知道是不安全的了,可以提前结束循环
                    if states[node] > 1:
                        break
                # 出的所有点为安全的，它才是安全的
                states[node] = 0 if states[node] == 1 else 2
            return states[node]

        return [i for i in range(n) if not dfs(i)]

        # n = len(graph)
        # # 每个点可能的状态: 安全的，不安全的
        # states = dict()
        #
        # def dfs(node):
        #     if node not in states:
        #         states[node] = False
        #         if all(dfs(nxt) for nxt in graph[node]):
        #             states[node] = True
        #     return states[node]
        #
        # return [i for i in range(n) if dfs(i)]
