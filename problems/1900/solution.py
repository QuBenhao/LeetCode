import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, firstPlayer, secondPlayer = test_input
        return self.earliestAndLatest(n, firstPlayer, secondPlayer)

    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        @lru_cache(None)
        def dfs(np, f, s):
            """
            :param np: number of players
            :param f: position of firstPlayer
            :param s: position of secondPlayer
            :return: tuple earliest, latest
            """
            # 对局为i对阵np-1-i
            if s + f == np - 1:
                return 1,1
            # 如果f在中间或者右侧,根据对称性,看成(np,np-1-s,np-1-f)
            if f >= np // 2:
                return dfs(np, np-1-s, np-1-f)
            # f 必然在左侧了
            # 判断s的位置
