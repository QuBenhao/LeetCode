import solution
from collections import defaultdict
from math import comb


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToBuildRooms(list(test_input))

    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        connect = defaultdict(list)
        for i, num in enumerate(prevRoom):
            connect[num].append(i)

        # Return: node count, number of topological orderings
        def dfs(idx):
            nodes, ans = 0, 1
            for subNode in connect[idx]:
                nodes_, ans_ = dfs(subNode)
                nodes += nodes_
                # The current ordering choices and the subtree's ordering choices are independent, so multiply them
                # New ordering count = current count * ways to choose nodes_ of nodes positions for this subtree * subtree ordering count
                ans = (ans * comb(nodes, nodes_) * ans_) % (10 ** 9 + 7)
            # Include the root
            return nodes + 1, ans

        return dfs(0)[1]
