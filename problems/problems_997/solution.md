# [Python/Java/JavaScript/Go] 入度出度统计

> Author: Benhao
> Date: 2021-12-19
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
只有存在一个人，即没出现在左边，且跟所有人都有在右边的关系的时候，返回这个人

### 代码

```python3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = list(zip(*trust))
        return ans[0] if trust and (ans := [i for i in range(1,n+1) if i not in l[0] and l[1].count(i) == n - 1]) else (1 if not trust and n == 1 else -1)
```
```Python3 []
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s, l = set(), [0] * n
        for a, b in trust:
            s.add(a)
            l[b-1] += 1
        for i in range(1, n + 1):
            if i not in s and l[i - 1] == n - 1:
                return i
        return -1
```
```Java []
class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] in = new int[n+1], out = new int[n+1];
        for(int[] t : trust) {
            out[t[0]]++;
            in[t[1]]++;
        }
        for(int i=1;i<=n;i++){
            if(out[i]==0 && in[i] == n - 1)
                return i;
        }
        return -1;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    const cnts = new Array(n + 1), out = new Array(n + 1)
    cnts.fill(0)
    out.fill(0)
    for(const t of trust){
        cnts[t[1]]++
        out[t[0]]++
    }
    for(let i = 1; i <= n; i++)
        if(out[i] == 0 && cnts[i] == n - 1)
            return i
    return -1
};
```
```Go []
func findJudge(n int, trust [][]int) int {
    in, out := make([]int, n + 1), make([]int, n + 1)
    for _, t := range trust {
        in[t[1]]++
        out[t[0]]++
    }
    for i := 1; i <= n; i++ {
        if out[i] == 0 && in[i] == n - 1 {
            return i
        }
    }
    return -1
}
```