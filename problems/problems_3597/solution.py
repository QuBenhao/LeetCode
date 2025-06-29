import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partitionString(test_input)

    def partitionString(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        root = {}

        def search(i):
            node = root
            for k in range(i, n):
                char = s[k]
                if char not in node:
                    node[char] = {"#": True}
                    ans.append(s[i:k+1])
                    return k + 1
                node = node[char]
            node["#"] = True
            return n

        start = 0
        while start < n:
            start = search(start)
        return ans
