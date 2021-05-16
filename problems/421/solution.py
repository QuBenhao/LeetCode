import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumXOR(list(test_input))

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        t = Trie(len(bin(max(nums))) - 2)
        for num in nums:
            ans = t.query(num, ans)
            t.insert(num)
        return ans


class Trie:
    def __init__(self, max_bit):
        self.root = {}
        self.max_bit = max_bit

    def insert(self, x):
        node = self.root
        for i in range(self.max_bit, -1, -1):
            bit = x >> i & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, x, high):
        node = self.root
        acc = 0
        g = False
        for i in range(self.max_bit, -1, -1):
            acc = acc << 1
            bit = x >> i & 1
            if not g:
                h_bit = high >> i & 1
            if 1 ^ bit in node:
                if not g and not h_bit:
                    g = True
                acc += 1
                node = node[1 ^ bit]
            elif bit in node:
                if not g and h_bit:
                    return high
                node = node[bit]
        return acc
