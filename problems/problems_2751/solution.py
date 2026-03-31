import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.survivedRobotsHealths(*test_input)

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # 按位置排序的机器人索引
        sorted_indices = sorted(range(len(positions)), key=lambda i: positions[i])

        survivors = {}  # {原始索引: 最终血量}
        right_going = []  # 栈: [血量, 原始索引]

        for i in sorted_indices:
            h, d = healths[i], directions[i]

            if d == 'R':
                right_going.append([h, i])
            else:  # 向左走，与栈中向右的机器人碰撞
                while right_going and h > 0:
                    top_h, top_i = right_going[-1]

                    if top_h > h:
                        right_going[-1][0] -= 1
                        h = 0
                    elif top_h < h:
                        right_going.pop()
                        h -= 1
                    else:
                        right_going.pop()
                        h = 0

                if h > 0:
                    survivors[i] = h

        # 栈中剩余的向右机器人
        for h, i in right_going:
            survivors[i] = h

        # 按原始位置顺序返回结果
        return [survivors[i] for i in sorted(survivors.keys())]

