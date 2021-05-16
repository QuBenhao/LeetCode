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
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        ans = [-1] * len(queries)
        j = 0
        for i, (n, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            ans[i] = trie.query(n)
        return ans


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]

    def query(self, num):
        if not self.root:
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans
