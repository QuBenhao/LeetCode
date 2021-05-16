import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, edges, queries = test_input
        return self.countPairs(n, [x[:] for x in edges], list(queries))

    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict

        ans = []

        nodeDegrees = [0] * (n + 1)
        edgeDegrees = defaultdict(int)

        # O(E)
        for u, v in edges:
            edgeDegrees[(min(u, v), max(u, v))] += 1
            nodeDegrees[u] += 1
            nodeDegrees[v] += 1

        # O(N logN)
        sortedNodeDegrees = sorted(nodeDegrees[1:])

        # O(K * (N + E))
        for q in queries:
            cnt = 0

            # Using two pointers, we can quickly compute `cnt`, which is the number of incident edges.
            # Notice that the cnt is over-counted because the shared edges between two points should be counted
            # for only once. We will adjust this later.
            tail = n
            for head in range(0, n - 1):
                tail = max(tail, head + 1)
                while tail - 1 > head and sortedNodeDegrees[head] + sortedNodeDegrees[tail - 1] > q:
                    tail -= 1
                cnt += n - tail

            # Adjust the `cnt`, for all the pairs of nodes that have shared edges, we check
            # 1) if it is being counted above, i.e., q < nodeDegrees[u] + nodeDegrees[v]
            # 2) if it should not be counted, i.e., nodeDegrees[u] + nodeDegrees[v] - edgeDegrees[(u, v)] <= q
            # If both of the two above is true, then we know this edge is being over counted, we reduce `cnt` by 1.
            for u, v in edgeDegrees:
                if nodeDegrees[u] + nodeDegrees[v] - edgeDegrees[(u, v)] <= q < nodeDegrees[u] + nodeDegrees[v]:
                    cnt -= 1

            ans.append(cnt)
        return ans
