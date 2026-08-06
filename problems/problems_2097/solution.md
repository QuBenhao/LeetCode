# [Python/Go] Hierholzer

> slug: pythongo-hierholzer-by-himymben-k0xl
> date: 2021-12-05
> tags: Go, Python, Python3
> question: Valid Arrangement of Pairs (valid-arrangement-of-pairs)
> url: https://leetcode.cn/problems/valid-arrangement-of-pairs/solutions/DfPBpK/pythongo-hierholzer-by-himymben-k0xl/

---
### 解题思路
进行一波算法学习记录，参考332题目的官解o(n)解决欧拉回路问题

### 代码

```python3 []
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        cnts = Counter()
        connect = defaultdict(list)
        for a, b in pairs:
            cnts[a] += 1
            cnts[b] -= 1
            connect[a].append(b)
        start = None
        for k, v in cnts.items():
            start = k
            # 入度比出度大一的点，必然作为起点
            if v == 1:
                break
        ans = []
        def dfs(u):
            # 遍历递归，直到遍历光
            while connect[u]:
                # 递归到尽头
                dfs(connect[u].pop())
            # 遍历光才加入当前节点
            ans.append(u)
        dfs(start)
        # 入栈顺序倒序必然是遍历路径
        return [[ans[i], ans[i-1]] for i in range(len(ans)-1,0,-1)]
```
```Go []
func validArrangement(pairs [][]int) [][]int {
    cnts := map[int]int{}
    connect := map[int][]int{}
    for _, pair := range pairs {
        a,b := pair[0], pair[1]
        cnts[a]++
        cnts[b]--
        connect[a] = append(connect[a], b)
    }

    start := 0
    for k, v := range cnts {
        start = k
        if v == 1{
            break
        }
    }
    ans := make([]int, 0)

    var dfs func(u int)
    dfs = func(u int){
        for n := len(connect[u]); n > 0; n = len(connect[u]) {
            v := connect[u][0]
            connect[u] = connect[u][1:]
            dfs(v)
        }
        ans = append(ans, u)
    }
    dfs(start)
    res := [][]int{}
    for i := len(ans)-1;i>0;i--{
        res = append(res, []int{ans[i], ans[i-1]})
    }
    return res
}
```