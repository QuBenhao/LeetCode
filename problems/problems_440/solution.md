# [Python/Java/JavaScript/Go] bfs + dfs

> Author: Benhao
> Date: 2022-03-22
> Upvotes: 58
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
考虑前缀树。
字典序会给我们这样一个顺序，
1作为根节点（前缀），子节点为10 - 19（以1为前缀）;
10作为根节点，子节点为100 - 109（以10为前缀）;
以此类推

我们需要找k属于哪个根节点下的哪个子节点。
假如1为根节点的全部的节点数都不够，那么bfs到2为根节点继续找

### 代码

```Python3 []
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 小于等于n的以1开头的数有多少个?
        # 1 10-19 100-199 1000-1999 = 1111
        def dfs(l, r):
            # 当前层有 r - l + 1 个节点可取，递归到下一层。
            # l * 10： 从10变成100， r * 10 + 9: 从19变成199
            return 0 if l > n else min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)
        
        cur = 1
        k -= 1
        while k:
            cnts = dfs(cur, cur)
            # 当前节点中总数都小于需要的数，可以全部取走，bfs到同层下一点 (比如 1 -> 2)
            if cnts <= k:
                k -= cnts
                cur += 1
            # 答案在当前节点的子节点中，取走当前根节点，dfs向下 (比如 1 -> 10)
            else:
                k -= 1
                cur *= 10
        return cur
```
```Java []
class Solution {
    public int findKthNumber(int n, int k) {
        int cur = 1;
        k--;
        while(k > 0) {
            long cnts = dfs(cur, cur, n);
            if(cnts <= k) {
                k -= cnts;
                cur++;
            } else {
                k--;
                cur *= 10;
            }
        }
        return cur;
    }

    private long dfs(long l, long r, int n) {
        if(l > n)
            return 0;
        return Math.min(r, n) - l + 1 + dfs(l * 10, r * 10 + 9, n);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    nn = BigInt(n)
    dfs = function(l, r) {
        if(l > nn)
            return 0n
        if(r > nn)
            r = nn
        return r - l + 1n + dfs(l * 10n, r * 10n + 9n)
    }
    cur = 1
    k--
    kn = BigInt(k)
    while(kn > 0) {
        cnts = dfs(BigInt(cur), BigInt(cur))
        if(cnts <= kn) {
            kn -= cnts
            cur += 1
        } else {
            kn -= 1n
            cur *= 10
        }
    }
    return cur
};
```
```Go []
func findKthNumber(n int, k int) int {
    var dfs func(l, r int) int
    dfs = func(l, r int) int {
        if l > n {
            return 0
        }
        if r > n {
            r = n
        }
        return r - l + 1 + dfs(l * 10, r * 10 + 9)
    }

    cur := 1
    k--
    for k > 0 {
        cnts := dfs(cur, cur)
        if cnts <= k {
            k -= cnts
            cur++
        } else {
            k--
            cur *= 10
        }
    }
    return cur
}
```