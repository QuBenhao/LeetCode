import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.carFleet(*test_input)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for p, s in sorted(zip(position, speed), key=lambda x: x[0]):
            # 避免除法精度运算
            # 左边更快到达的, 一定会和右边更慢到达的形成一个元素, 即单调递增栈
            while st and st[-1][0] * s <= (target - p) * st[-1][1]:
                st.pop()
            st.append(((target - p), s))
        return len(st)
