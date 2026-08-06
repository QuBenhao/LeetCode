# [Python/Go] 集合交集、并集 or 并查集

> slug: pythongo-ji-he-jiao-ji-bing-ji-by-himymb-4l1o
> date: 2021-11-14
> tags: Go, Python, Python3
> question: Process Restricted Friend Requests (process-restricted-friend-requests)
> url: https://leetcode.cn/problems/process-restricted-friend-requests/solutions/Ukx1oj/pythongo-ji-he-jiao-ji-bing-ji-by-himymb-4l1o/

---
### 解题思路
爱一个人，也要爱一个人的优点和缺点。成为朋友，就接纳了ta的全部

### 代码

```python3 []
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        groups = defaultdict(set)
        group_b = defaultdict(set)
        for i in range(n):
            groups[i].add(i)
        for a,b in restrictions:
            group_b[a].add(b)
            group_b[b].add(a)
        result = [False] * len(requests)
        for i,v in enumerate(requests):
            a,b = v
            if a in groups and b in groups[a]:
                result[i] = True
                continue
            if (group_b[b] & groups[a]) or (group_b[a] & groups[b]):
                continue
            group_b[a] |= group_b[b]
            groups[a] |= groups[b]
            for aa in groups[a]:
                groups[aa] = groups[a]
                group_b[aa] = group_b[a]
            result[i] = True
        return result
```
```Go []
func friendRequests(n int, restrictions [][]int, requests [][]int) []bool {
    f := make([]int, n)
    for i := range f {
        f[i] = i
    }

    var find func(x int)int
    find = func(x int) int {
        if x == f[x] {
            return x
        }
        return find(f[x])
    }

    restrict := make([]map[int]bool, n)
    for i := range restrict {
        restrict[i] = map[int]bool{}
    }
    for _, r := range restrictions {
        x, y := r[0], r[1]
        restrict[x][y] = true
        restrict[y][x] = true
    }

    ans := make([]bool, len(requests))
    for i, r := range requests {
        x, y := find(r[0]), find(r[1])
        if x == y {
            ans[i] = true
            continue
        }
        if restrict[x][y] {
            continue
        }
        ans[i] = true
        if len(restrict[x]) > len(restrict[y]) {
            x, y = y, x
        }
        for xx := range restrict[x]{
            xx = find(xx)
            restrict[y][xx] = true
            restrict[xx][y] = true
        }
        f[x] = y
    }
    return ans
}
```