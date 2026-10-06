import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.braceExpansionII(test_input)

    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def dfs(i: int) -> tuple[set[str], int]:
            """Parse a comma-separated list of alternatives, stopping at '}' or the end.

            Return (the union of the alternatives, the stopping index pointing to '}' or the end).
            """
            alts: set[str] = set()
            prod = {""}  # Concatenation result for the current alternative
            while i < n and expression[i] not in ",}":
                if expression[i] == "{":
                    sub, i = dfs(i + 1)  # Union of the subgroup
                    prod = {a + b for a in prod for b in sub}
                    i += 1  # Skip '}'
                else:
                    prod = {a + expression[i] for a in prod}
                    i += 1
            alts |= prod  # Final alternative
            if i < n and expression[i] == ",":
                rest, i = dfs(i + 1)  # More alternatives follow the comma; take their union at the same level
                alts |= rest
            return alts, i

        res, _ = dfs(0)
        return sorted(res)
