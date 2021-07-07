import solution
from collections import Counter


class Solution(solution.Solution):
    # powersOfTwo = [2 ** i for i in range(22)]
    # mod = 10 ** 9 + 7

    def solve(self, test_input=None):
        return self.countPairs(list(test_input))

    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        # cnts = Counter(deliciousness)
        # return (sum(
        #     cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target - key]
        #     for key in cnts for target in self.powersOfTwo)) // 2 % self.mod

        MOD = 1000000007
        count = Counter(deliciousness)

        res = 0
        # 由于每个数只遍历了最接近自己的2的次幂的组合，所以不可能重复;比如说1和3构成4，只在3的时候计算；3和5构成8只在5的时候计算。
        for i in count:
            if i == 0:
                continue
            # i的下一个2的幂次
            target = self.nextPower(i)
            # 如果i能和任意的count中的key够成这个幂次
            res += count[i] * count[target - i]
            # 如果i自身是一个2的幂次
            if i == target:
                res += count[i] * (count[i] - 1) // 2
        return res % MOD

    def nextPower(self, x: int):
        x -= 1
        x |= x >> 1
        x |= x >> 2
        x |= x >> 4
        x |= x >> 8
        x |= x >> 16
        return x + 1
