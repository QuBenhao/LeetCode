import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.intersectionSizeTwo(test_input)

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 右端点从小到大，保证贪心处理边缘点的正确性，同时右端点一样的时候优先处理长度最短的区间，因为该区间可选点最少同时会覆盖其他区间
        intervals.sort(key=lambda x: (x[1], -x[0]))
        # 由于我们是单调递增添加元素，维护当前集合前二大的元素即可判断是否需要添加新的
        a, b, ans = -1, -1, 0
        for left, right in intervals:
            # 如果区间左端点也在当前最大元素的右边，说明需要从该区间添加两个新点(可以理解为递归，前面的不再起作用)
            if left > b:
                # 贪心取最大的两个点
                a, b, ans = right - 1, right, ans + 2
            # 如果区间左端点位于当前最大元素与次大元素的中间，说明最大元素本身是区间内的一个点了
            elif left > a:
                # 我们还需要再取一个，贪心取该区间最大，原来的b成为次大
                a, b, ans = b, right, ans + 1
        return ans
