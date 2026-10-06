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
        #         # Count every node's outdegree
        #         out[i] += 1
        # q = deque([])
        # for i in range(n):
        #     if not out[i]:
        #         # Enqueue nodes with outdegree 0
        #         q.append(i)
        # while q:
        #     node = q.popleft()
        #     for front in edges[node]:
        #         # Remove the edge front->node
        #         out[front] -= 1
        #         if not out[front]:
        #             # If removing the edge makes front's outdegree 0, enqueue it
        #             q.append(front)
        # return [i for i in range(n) if not out[i]]

        n = len(graph)
        # Node states: -1: unvisited, 0: safe, 1: visited but safety undetermined, 2: unsafe
        states = [-1] * n

        def dfs(node):
            # Not yet visited
            if states[node] == -1:
                # Mark as state 1
                states[node] = 1
                for nxt in graph[node]:
                    states[node] += dfs(nxt)
                    # Already known to be unsafe; stop the loop early
                    if states[node] > 1:
                        break
                # A node is safe only if all its successors are safe
                states[node] = 0 if states[node] == 1 else 2
            return states[node]

        return [i for i in range(n) if not dfs(i)]

        # n = len(graph)
        # # Node states: safe or unsafe
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
