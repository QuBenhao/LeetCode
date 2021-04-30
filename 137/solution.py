import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNumber(test_input.copy())

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 位数统计
        # cnt = [0] * 32
        # for num in nums:
        #     for i in range(32):
        #         # 最右边第i位是否为1
        #         if (num >> i) & 1:
        #             cnt[i] += 1
        # ans = 0
        # for i in range(32):
        #     if cnt[i] % 3:
        #         # Python 中第32位为1表示负数
        #         if i == 31:
        #             ans -= (1 << i)
        #         else:
        #             ans += (1 << i)
        # return ans

        """
        真值表转换解法
        00 - 出现一次 -> 01 - 出现一次 -> 10 - 出现一次 -> 00
        用两位a和b表示三种状态的值，我们有:
        a,b,x -> a b
        0 0 0 -> 0 0
        0 0 1 -> 0 1
        0 1 0 -> 0 1
        0 1 1 -> 1 0
        1 0 0 -> 1 0
        1 0 1 -> 0 0
        也就是说:
        同时更新a,b的话:
        a, b = (a & ~x) | (b & x), b ^ x & ~a
        
        先更新b，用新的b更新a的话:
        b = b ^ x & ~a
        a = a ^ x & ~b
        """
        a = b = 0
        for num in nums:
            # a, b = (a & ~num) | (b & num), b ^ num & ~a
            b = b ^ num & ~a
            a = a ^ num & ~b
        return b
