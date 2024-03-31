import solution
from typing import *
import itertools

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.letterCasePermutation(test_input)

    def letterCasePermutation(self, s: str) -> List[str]:
        return list(map(''.join, itertools.product(*[{i.lower(), i.upper()} for i in s])))

        # # These code are doing the same thing as [set([i.lower, i.upper()]) for i in s]
        # iters = []
        # for c in s:
        #     if c.isalpha():
        #         iters.append([c.lower(), c.upper()])
        #     else:
        #         iters.append([c])
        # return list(map(''.join, itertools.product(*iters)))

        # ans, n = [], len(s)
        #
        # def dfs(string, index):
        #     if index == n:
        #         ans.append(string)
        #         return
        #     dfs(string[:index]+S[index], index + 1)
        #     if s[index].isalpha():
        #         if S[index].islower():
        #             dfs(string[:index]+S[index].upper(), index + 1)
        #         else:
        #             dfs(string[:index]+S[index].lower(), index + 1)
        #
        # dfs("", 0)
        # return ans
