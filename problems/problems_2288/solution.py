import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.discountPrices(*test_input)


    def discountPrices(self, sentence: str, discount: int) -> str:
        ans = []
        for s in sentence.split(" "):
            if len(s) > 1 and s.startswith("$"):
                cur = 0
                for i in range(1, len(s)):
                    if not s[i].isdigit():
                        break
                    cur = 10 * cur + ord(s[i]) - ord('0')
                else:
                    ans.append("$%.2f" % (cur * (100 - discount) / 100))
                    continue
            ans.append(s)
        return " ".join(ans)

