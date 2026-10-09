import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.braceExpansionII(test_input)

    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def dfs(i: int) -> tuple[set[str], int]:
            alts: set[str] = set()
            prod = {""}  # 当前备选的连接结果
            while i < n and expression[i] not in ",}":
                if expression[i] == "{":
                    sub, i = dfs(i + 1)  # 子组的并集
                    prod = {a + b for a in prod for b in sub}
                    i += 1  # 跳过 '}'
                else:
                    prod = {a + expression[i] for a in prod}
                    i += 1
            alts |= prod  # 最后一个备选
            if i < n and expression[i] == ",":
                rest, i = dfs(i + 1)  # 逗号后面还有备选，同级并集
                alts |= rest
                alts |= rest
            return alts, i

        res, _ = dfs(0)
        return sorted(res)
