# [Python/Java] 回溯 + Trie删除

> Author: Benhao
> Date: 2021-09-15
> Upvotes: 14
> Tags: Java, Python, Python3

---

### 解题思路
单纯的dfs回溯超时了。采用统计单词字母个数加速，比如某个单词要10个'e'，棋盘上一共9个'e'，那必然不能构成这个单词

**更新于2024/04/06**
回溯遍历时更新找到过的单词，移出Trie

### 代码

```python3 []
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
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

```
```Java []
class Solution {
    int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    char[][] bd;
    int m, n;
    public List<String> findWords(char[][] board, String[] words) {
        bd = board;
        m = board.length;
        n = board[0].length;
        int[] cnts = new int[26];
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                cnts[board[i][j] - 'a']++;
        List<String> ans = new ArrayList<>();
        for(String word:words){
            int[] cur = new int[26];
            for(char c:word.toCharArray())
                cur[c - 'a']++;
            boolean valid = true;
            for(int i = 0; i < 26; i++)
                if(cnts[i] < cur[i]){
                    valid = false;
                    break;
                }
            if(!valid)
                continue;
            boolean find = false;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++)
                    if(dfs(word, 0, i, j, new HashSet<Integer>())){
                        find = true;
                        ans.add(word);
                        break;
                    }
                if(find)
                    break;
            }
        }
        return ans;
    }

    public boolean dfs(String word, int idx, int x, int y, Set<Integer> explored){
        if(idx == word.length())
            return true;
        Integer pos = x * n + y;
        if(explored.contains(pos) || x < 0 || y < 0 || x == m || y == n)
            return false;
        if(bd[x][y] == word.charAt(idx++)){
            explored.add(pos);
            for(int[] dir: dirs)
                if(dfs(word, idx, x + dir[0], y + dir[1], explored))
                    return true;
            explored.remove(pos);
        }
        return false;
    }
}
```