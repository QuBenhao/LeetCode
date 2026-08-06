# [Python] 差分数组

> slug: python-cha-fen-shu-zu-by-himymben-v28w
> date: 2022-05-04
> tags: Python, Python3
> question: Average Height of Buildings in Each Segment (average-height-of-buildings-in-each-segment)
> url: https://leetcode.cn/problems/average-height-of-buildings-in-each-segment/solutions/NqAMMO/python-cha-fen-shu-zu-by-himymben-v28w/

---
### 解题思路
差分扫描线问题

### 代码

```python3
class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        cnts = defaultdict(int)
        for a, b, h in buildings:
            diff[a] += h
            diff[b] -= h
            cnts[a] += 1
            cnts[b] -= 1
        cur, cnt, last, last_p, ans = 0, 0, None, None, []
        for k in sorted(diff.keys()):
            cur += diff[k]
            if last:
                if ans and ans[-1][1] == last_p and ans[-1][2] == last // cnt:
                    ans[-1][1] = k
                else:
                    ans.append([last_p, k, last // cnt])
            cnt += cnts[k]
            last, last_p = cur, k
        return ans
```