import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        destination, k = test_input
        return self.kthSmallestPath(list(destination), k)

    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        # 本题为组合题，有h个相同的'H'和v个相同的'V',我们需要对他们进行排序
        # 队列长度为h+v,我们需要选择h个位置给'H'
        # 也就是说对h,v来说，组合数有comb(h+v,h)个
        v, h = destination
        res = ''
        while h > 0 and v > 0:
            # 先选'H'的选择比先选'V'的选择优先，那么在h,v位置，选'H'的话，h-1,v不变
            # 此处放'H'的组合数
            num = math.comb(h + v - 1, h - 1)
            # 如果放'H'都不足以凑够k个，说明这里要放V，然后在后面找k-num
            if k > num:
                res += 'V'
                v -= 1
                k -= num
            # 如果足够k个了，说明这里是放'H'的，到后面继续判断该'H'还是'V'
            else:
                res += 'H'
                h -= 1
        # 我们到达了某个边，剩下的就是只有一种情况（走到尽头即可）
        return res + h * 'H' + v * 'V'
