import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRedundantDirectedConnection(test_input)

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 更新x的所属节点，并返回编号为x的所属节点
        def find(x: int) -> int:
            # 如果x已经为根节点了，直接返回
            # 否则就沿着所属根节点一直往上走
            if x == pa[x]:
                return x
            pa[x] = find(pa[x])
            return pa[x]

        # 合并两个节点所属区域
        def unit(x: int, y: int):
            # 将y的所属节点作为x所属节点的所属节点
            # 相当于x所在的这个子树搭到y的所在子树的根节点上
            pa[find(x)] = find(y)

        n = len(edges)
        pa = list(range(n + 1))  # pa[i]表示节点i的所属根节点，用于并查集; 初始pa[i]=i，表示节点i以自己为根节点
        fa = list(range(n + 1))  # fa[i]表示节点i的父节点; 初始fa[i]=i，表示节点i的父节点为本身

        conflict = -1  # 冲突边的下标，初始为-1，表示不存在冲突
        circle = -1  # 构成环的下标，初始为-1，表示不存在环
        for i, (a, b) in enumerate(edges):
            if fa[b] != b:
                conflict = i  # 找到冲突的边，这个边我们就不会加入并查集
            else:
                fa[b] = a  # 记录节点b的父节点为a
                if find(a) != find(b):
                    unit(a, b)  # 如果两个节点不在一个树上，则合并
                else:
                    circle = i  # 如果两个节点已经在一个树上，则这条边就是构成环的最后一条边

        if conflict < 0:
            return edges[circle]  # 有环无冲突，直接返回构成环的最后一条边
        if circle < 0:
            return edges[conflict]  # 有冲突无环，删掉冲突的边
        b = edges[conflict][1]
        return [fa[b], b]  # 有环有冲突，冲突的另一条边一定在环上，删除它
