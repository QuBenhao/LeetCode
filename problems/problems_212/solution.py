import solution
from typing import *

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findWords(*test_input)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = dict()
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node["#"] = dict()

        def dfs(nd, path, trie_path, i, j):
            if board[i][j] not in nd:
                return
            c = board[i][j]
            nd = nd[c]
            path.append(c)
            trie_path.append((c, nd))
            board[i][j] = "#"
            if "#" in nd:
                s = "".join(path)
                ans.append(s)
                nd.pop("#")
                for x in range(len(trie_path) - 1, 0, -1):
                    if len(trie_path[x][1]) == 0:
                        trie_path[x - 1][1].pop(trie_path[x][0])
                    else:
                        break
            for di, dj in DIRS:
                if 0 <= (ni := i + di) < m and 0 <= (nj := j + dj) < n:
                    dfs(nd, path, trie_path, ni, nj)
            path.pop()
            trie_path.pop()
            board[i][j] = c

        ans = []
        for i in range(m):
            for j in range(n):
                dfs(trie, [], [("", trie)], i, j)
        return ans
