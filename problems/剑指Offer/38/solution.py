import solution
from itertools import permutations
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.permutation(str(test_input))

    # def permutation(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     return list(set(''.join(st) for st in permutations(s)))

    # @lru_cache(None)
    # def permutation(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     # 递归解法
    #     if len(s) <= 1:
    #         return [s]
    #     return list(set(s[i] + perm for i in range(len(s)) for perm in self.permutation(s[:i] + s[i + 1:])))

    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 非递归解法
        n = len(s)
        curr = list(sorted(s))
        end = list(reversed(curr))
        ans = []
        # 生成下一个排列
        while curr != end:
            ans.append(''.join(curr))
            i = n - 2
            # 29631 -> 31269
            while i > 0:
                if curr[i] < curr[i + 1]:
                    break
                i -= 1
            j = n - 1
            while j > i - 1:
                if curr[j] > curr[i]:
                    break
                j -= 1
            curr[i], curr[j] = curr[j], curr[i]
            curr = curr[:i + 1] + sorted(curr[i + 1:])
        ans.append(''.join(end))
        return ans
