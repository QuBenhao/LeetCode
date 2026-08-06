# [Python] 状态压缩并查集

> slug: python-zhuang-tai-ya-suo-bing-cha-ji-by-drrvu
> date: 2022-01-30
> tags: Python, Python3
> question: Groups of Strings (groups-of-strings)
> url: https://leetcode.cn/problems/groups-of-strings/solutions/cpubag/python-zhuang-tai-ya-suo-bing-cha-ji-by-drrvu/

---
### 解题思路
终于学会了并查集。

### 代码
```python3
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        @lru_cache(None)
        def helper(s):
            res = 0
            for c in s:
                res |= 1 << (ord(c) - ord('a'))
            return res
            
        n = len(words)
        f = [i for i in range(n)]
        rank = [1] * n

        # 路径合并
        def find(x):
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        
        # 按秩合并
        def union(x, y):
            fx, fy = find(x), find(y)
            if rank[fx] <= rank[fy]:
                f[fx] = fy
            else:
                f[fy] = fx
            if rank[fx] == rank[fy] and fx != fy:
                rank[fy] += 1
        
        idx_map = dict()
        for i, w in enumerate(words):
            if helper(w) in idx_map:
                union(idx_map[helper(w)], i)
            idx_map[helper(w)] = i
        
        for k in range(n):
            tp = helper(words[k])
            for i in range(26):
                # 删除当前位
                if (tp >> i) & 1:
                    cur = tp ^ (1 << i)
                    if cur in idx_map:
                        union(k, idx_map[cur])
                    # 替换
                    for j in range(26):
                        if not ((tp >> j) & 1):
                            cur ^= 1 << j
                            if cur in idx_map:
                                union(k, idx_map[cur])
                            cur ^= 1 << j
        
        ans = defaultdict(int)
        for i in range(n):
            ans[find(i)] += 1
        return [len(ans), max(ans.values())]
```

