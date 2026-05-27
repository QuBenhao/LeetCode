from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stringIndices(*test_input)

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ord_a = ord('a')
        root = Node()
        for i, s in enumerate(wordsContainer):
            len_s = len(s)
            if len_s < root.min_len:
                root.min_len = len_s
                root.best_index = i

            # 把 s[::-1] 插入字典树
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    cur.son[c] = Node()
                cur = cur.son[c]
                # 维护 cur 子树中的最短字符串的长度及其下标
                # 由于我们是按照 i 从小到大的顺序遍历，字符串长度相同时不更新 best_index
                if len_s < cur.min_len:
                    cur.min_len = len_s
                    cur.best_index = i

        ans = []
        for s in wordsQuery:
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            # 退出循环时，cur 即最长公共前缀（的对应节点），cur.best_index 是前缀为 cur 的最短字符串的下标
            ans.append(cur.best_index)
        return ans

class Node:
    __slots__ = 'son', 'min_len', 'best_index'

    def __init__(self):
        self.son = [None] * 26
        self.min_len = inf  # 子树中的最短字符串的长度
