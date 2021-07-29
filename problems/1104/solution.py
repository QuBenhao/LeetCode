import solution
from math import log


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pathInZigZagTree(label=test_input)

    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        ans = [label]
        # 初始入口端点
        last = 2 ** int(log(label, 2))
        while label > 1:
            # 上一层节点到其出口端点的距离
            add = label - last >> 1
            # 计算父亲节点的值
            label = last - 1 - add
            # 下一个入口端点必然是除以2的关系
            last >>= 1
            ans.append(label)
        return ans[::-1]

        # ans = [label]
        # # 初始出口端点
        # last = 2 ** (int(log(label, 2)) + 1)
        # while label > 1:
        #     # 上一层节点到其入口端点的距离
        #     dis = last - 1 - label >> 1
        #     # 计算父亲节点的值
        #     label = last // 4 + dis
        #     # 下一个出口端点必然是除以2的关系
        #     last >>= 1
        #     ans.append(label)
        # return ans[::-1]
