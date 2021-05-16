import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, low, high = test_input
        return self.countPairs(list(nums), low, high)

    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        def test(A, x):
            count = Counter(A)
            res = 0
            while x:
                # x的最后一位为1
                if x & 1:
                    # a ^ (x-1) ^ a 的结果为x-1,必然小于x
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                # 往右移一位，新的a>>1 由 a^0和a^1组成
                count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2
        return test(nums, high + 1) - test(nums, low)

        # trie = Trie()
        #
        # ans = 0
        # for x in nums:
        #     ans += trie.count(x, high + 1) - trie.count(x, low)
        #     trie.insert(x)
        # return ans


# class Trie:
#     def __init__(self):
#         self.root = {}
#
#     def insert(self, val):
#         node = self.root
#         for i in reversed(range(15)):
#             # every bit of the val from left to right
#             bit = (val >> i) & 1
#             if bit not in node:
#                 node[bit] = {"cnt": 1}
#             else:
#                 node[bit]["cnt"] += 1
#             node = node[bit]
#
#     def count(self, val, high):
#         ans = 0
#         node = self.root
#         for i in reversed(range(15)):
#             if not node:
#                 break
#             # every bit of the val and high from left to right
#             bit = (val >> i) & 1
#             cmp = (high >> i) & 1
#             # 如果high的第i位是1
#             if cmp:
#                 # 如果当前字典中存在和bit值相等的，也就是该位异或结果为0，是小于此时cmp的1的,应直接加入答案
#                 if node.get(bit, {}):
#                     ans += node[bit]["cnt"]
#                 # 当前字典中存在和bit值异或为1的，也就是和cmp相等，那么要比较下一位的结果
#                 node = node.get(1 ^ bit, {})
#             else:
#                 # 当前cmp为0，只有和bit异或结果为0的可以加入答案
#                 node = node.get(bit, {})
#         return ans
