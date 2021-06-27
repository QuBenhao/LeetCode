import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wonderfulSubstrings(str(test_input))

    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # 每个位置i需要表示从0到i里，从a到j的个数的奇偶性，故采用10位二进制字符串，0表示该位为偶数，1表示该位为奇数
        # 记录从0到i的个数的二进制字符串
        ans = mask = 0
        # 统计到目前为止各种二进制字符串的个数, 什么也不选的为1个
        freq = defaultdict(int, {0:1})
        for c in word:
            u = ord(c) - ord('a')
            # 更新当前字符的个数的奇偶性
            mask ^= 1 << u
            for i in range(10):
                # 只有第i位不同的字符串的个数，也就是说从当前位置到该位置，i的个数为奇数个
                ans += freq[mask ^ 1 << i]
            # 所有字符均出现偶数次的个数
            ans += freq[mask]
            freq[mask] += 1
        return ans
