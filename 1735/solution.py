import solution
from functools import lru_cache
from collections import Counter
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToFillArray([x[:] for x in test_input])

    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # target最大为10000，那么质因数最大为97
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        # 分解质因数
        @lru_cache(None)
        def div(num):
            c = Counter()
            for i in primes:
                while num % i == 0:
                    c[i] += 1
                    num //= i
            if num > 1:
                c[num] += 1
            return c

        ans = []
        for l,t in queries:
            count = div(t)
            cur = 1
            # 对于每个质因子，分配方式为将v个质因数填入l个箱子中有多少种填法
            # 球同，盒不同，盒可以为空，组合数结果为C(N+M-1, M-1)
            for v in count.values():
                cur *= math.comb(l+v-1,v)
            ans.append(cur % (10 ** 9 + 7))
        return ans
