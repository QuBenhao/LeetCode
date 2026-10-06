import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPairs(*test_input)

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
                # The last bit of x is 1
                if x & 1:
                    # a ^ (x-1) ^ a equals x-1, which is necessarily less than x
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                # Shift right by one bit; the new a>>1 combines contributions from a^0 and a^1
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
#             # If bit i of high is 1
#             if cmp:
#                 # An entry matching bit gives XOR 0, below cmp's 1; add it directly to the answer
#                 if node.get(bit, {}):
#                     ans += node[bit]["cnt"]
#                 # An entry giving XOR 1 matches cmp, so compare the next bit
#                 node = node.get(1 ^ bit, {})
#             else:
#                 # With cmp equal to 0, only entries giving XOR 0 can contribute
#                 node = node.get(bit, {})
#         return ans
