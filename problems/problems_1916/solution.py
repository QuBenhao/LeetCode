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

        # 返回:元素个数,拓扑排序方案数
        def dfs(idx):
            nodes, ans = 0, 1
            for subNode in connect[idx]:
                nodes_, ans_ = dfs(subNode)
                nodes += nodes_
                # 因为当前的拓扑排序方案数不影响加入该子树后的拓扑排序方案数，所以是乘法叠加
                # 新的拓扑排序方案数为: 当前的拓扑排序方案数 * 从nodes个位置里选nodes_个位置分配给该子树 * 子树的拓扑排序方案数
                ans = (ans * comb(nodes, nodes_) * ans_) % (10 ** 9 + 7)
            # 加上根节点
            return nodes + 1, ans

        return dfs(0)[1]
