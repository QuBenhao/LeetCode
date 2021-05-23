import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, queries = test_input
        return self.maximizeXor(list(nums),[x[:] for x in queries])

    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        """
        The idea behind this problem comes from LC 421 and LC 1697.

        Similar to LC 421, we can convert each number to binary format and construct a trie that has children of 0 
        and 1. In this way, we can query the maximum bitwise XOR value in O(32) time. 
        
        Similar to LC 1697, we can sort queries and construct the trie on the fly. 
        We use a two pointer approach to make sure only elements that do not exceed m_i are added to the trie.
        
        Putting these thoughts together, we arrive at the solution below. Please refer to the code for more details.
        """
        nums.sort()
        qrs = sorted(enumerate(queries),key=lambda x:x[1][1])
        trie = Trie()
        idx, n = 0, len(nums)
        ans = [0] * len(qrs)
        for i,(x, m) in qrs:
            while idx < n and nums[idx] <= m:
                trie.add(nums[idx])
                idx += 1
            ans[i] = trie.query(x)
        return ans


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, x):
        node = self.root
        for i in range(31, -1, -1):
            bit = x >> i & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, x):
        res = 0
        node = self.root
        for i in range(31, -1, -1):
            res <<= 1
            bit = x >> i & 1
            xor = bit ^ 1
            if xor in node:
                res += 1
                node = node[xor]
            elif bit in node:
                node = node[bit]
            else:
                return -1
        return res
