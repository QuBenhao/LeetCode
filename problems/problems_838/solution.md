# [Python/Java/JavaScript/Go] 正反遍历模拟

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 35
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
我们要统计所有点最近的'L'和'R'，来判断最终该点的状态。
如果‘L’更近，最终为'L'；如果'R'更近，最终为'R'；如果一样近，最终为'.'

> 从左往右遍历时，遇到'R'，更新最新的'R'起点；遇到'L'，将'R'起点更新为无限远；每个点的'R'距离由它的坐标和'R'起点的坐标计算得到。
> 从右往左遍历时，遇到'L'，更新最新的'L'起点；遇到'R'，将'L'起点更新为无限远；每个点的'L'距离由它的坐标和'L'起点的坐标计算得到。

### 代码

```Python3 []
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        # [L_dist, R_dist]
        records = [[inf, inf] for _ in range(n)]
        cur = -inf
        for i, c in enumerate(dominoes):
            if c == 'R':
                cur = i
            elif c == 'L':
                cur = -inf
            records[i][1] = i - cur
        cur = inf
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                cur = i
            elif dominoes[i] == 'R':
                cur = inf
            records[i][0] = cur - i
        return "".join('.' if l == r else ('R' if l > r else 'L') for l, r in records)
```
```Java []
class Solution {
    private static final int INF = 0x3f3f3f;
    public String pushDominoes(String dominoes) {
        int n = dominoes.length();
        int[][] records = new int[n][2];
        for(int i = 0, cur = -INF; i < n; i++) {
            char c = dominoes.charAt(i);
            if(c == 'R')
                cur = i;
            else if(c == 'L')
                cur = -INF;
            records[i][1] = cur == -INF ? INF : i - cur;
        }
        for(int i = n - 1, cur = INF; i >= 0; i--) {
            char c = dominoes.charAt(i);
            if(c == 'L')
                cur = i;
            else if(c == 'R')
                cur = INF;
            records[i][0] = cur == INF ? INF : cur - i;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            if(records[i][0] == records[i][1])
                sb.append('.');
            else if(records[i][0] > records[i][1])
                sb.append('R');
            else
                sb.append('L');
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {string} dominoes
 * @return {string}
 */
const INF = 0x3f3f3f
var pushDominoes = function(dominoes) {
    const n = dominoes.length, records = new Array(dominoes.length)
    for(let i = 0, cur = -INF; i < n; i++) {
        records[i] = new Array(2)
        if(dominoes.charAt(i) == 'R')
            cur = i
        else if(dominoes.charAt(i) == 'L')
            cur = -INF
        records[i][1] = cur == -INF ? INF : i - cur
    }
    for(let i = n - 1, cur = INF; i >= 0; i--) {
        if(dominoes.charAt(i) == 'L')
            cur = i
        else if(dominoes.charAt(i) == 'R')
            cur = INF
        records[i][0] = cur == INF ? INF : cur - i        
    }
    const ans = new Array()
    for(let i = 0; i < n; i++) {
        if(records[i][0] == records[i][1])
            ans.push('.')
        else if(records[i][0] < records[i][1])
            ans.push('L')
        else
            ans.push('R')
    }
    return ans.join("")
};
```
```Go []
const INF int = 0x3f3f3f
func pushDominoes(dominoes string) string {
    n, records := len(dominoes), make([][]int, len(dominoes))
    for i, cur := 0, -INF; i < n; i++ {
        records[i] = make([]int, 2)
        if dominoes[i] == 'R' {
            cur = i
        } else if dominoes[i] == 'L' {
            cur = -INF
        }
        if cur == -INF {
            records[i][1] = INF
        } else {
            records[i][1] = i - cur
        }
    }
    for i, cur := n - 1, INF; i >= 0; i-- {
        if dominoes[i] == 'L' {
            cur = i
        } else if dominoes[i] == 'R' {
            cur = INF
        }
        if cur == INF {
            records[i][0] = INF
        } else {
            records[i][0] = cur - i
        }
    }
    ans := make([]byte, n)
    for i, r := range records {
        if r[0] == r[1] {
            ans[i] = '.'
        } else if r[0] > r[1] {
            ans[i] = 'R'
        } else {
            ans[i] = 'L'
        }
    }
    return string(ans)
}

```