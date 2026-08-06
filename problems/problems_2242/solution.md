# [Python] 关于装饰器缓存的教训

> slug: python-guan-yu-by-himymben-5y0m
> date: 2022-04-16
> tags: Python, Python3
> question: Maximum Score of a Node Sequence (maximum-score-of-a-node-sequence)
> url: https://leetcode.cn/problems/maximum-score-of-a-node-sequence/solutions/3zhVnX/python-guan-yu-by-himymben-5y0m/

---
### 解题思路
暴力枚举中间的那条边，统计两头能给找到的其他最大得分点。

装饰器返回的缓存对象一定不要直接编辑！会改变缓存结果。加两个list复制比赛代码就ac了😓

### 代码
```python3
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        vs = dict()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            vs[(a, b)] = scores[a] + scores[b]
        
        n = len(graph)
        
        @lru_cache(None)
        def get_max_two(x):
            res = [None] * 3
            for ox in graph[x]:
                if res[0] is None:
                    res[0] = ox
                elif scores[res[0]] < scores[ox]:
                    res[2] = res[1]
                    res[1] = res[0]
                    res[0] = ox
                elif res[1] is None:
                    res[1] = ox
                elif scores[res[1]] < scores[ox]:
                    res[2] = res[1]
                    res[1] = ox
                elif res[2] is None or scores[res[2]] < scores[ox]:
                    res[2] = ox
            return res

        ans = -1
        for a, b in vs.keys():
            if len(graph[a]) > 1 and len(graph[b]) > 1:
                ma = list(get_max_two(a))
                for i in range(len(ma)):
                    if ma[i] == b:
                        ma.pop(i)
                        break
                mb = list(get_max_two(b))
                for i in range(len(mb)):
                    if mb[i] == a:
                        mb.pop(i)
                        break
                if ma[1] is None and mb[1] is None:
                    if ma[0] != mb[0]:
                        ans = max(ans, vs[(a, b)] + scores[ma[0]] + scores[mb[0]])
                elif ma[1] is None:
                    if ma[0] == mb[0]:
                        ans = max(ans, vs[(a, b)] + scores[ma[0]] + scores[mb[1]])
                    else:
                        ans = max(ans, vs[(a, b)] + scores[ma[0]] + scores[mb[0]])
                elif mb[1] is None:
                    if ma[0] == mb[0]:
                        ans = max(ans, vs[(a, b)] + scores[ma[1]] + scores[mb[0]])
                    else:
                        ans = max(ans, vs[(a, b)] + scores[ma[0]] + scores[mb[0]])
                else:
                    if ma[0] == mb[0]:
                        ans = max(ans, vs[(a, b)] + scores[ma[1]] + scores[mb[0]], vs[(a, b)] + scores[ma[0]] + scores[mb[1]])
                    else:
                        ans = max(ans, vs[(a, b)] + scores[ma[0]] + scores[mb[0]])
        return ans
```