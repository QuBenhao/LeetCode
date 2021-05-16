import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.letterCasePermutation(str(test_input))

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        import itertools
        # # These code are doing the same thing as [set([i.lower, i.upper()]) for i in S]
        # iters = []
        # for c in S:
        #     if c.isalpha():
        #         iters.append([c.lower(), c.upper()])
        #     else:
        #         iters.append([c])
        # return list(map(''.join, itertools.product(*iters)))
        return list(map(''.join, itertools.product(*[{i.lower(), i.upper()} for i in S])))

        # ans, n = [], len(S)
        #
        # def dfs(string, index):
        #     if index == n:
        #         ans.append(string)
        #         return
        #     dfs(string[:index]+S[index], index + 1)
        #     if S[index].isalpha():
        #         if S[index].islower():
        #             dfs(string[:index]+S[index].upper(), index + 1)
        #         else:
        #             dfs(string[:index]+S[index].lower(), index + 1)
        #
        # dfs("", 0)
        # return ans
