# [Python/Java/JavaScript/Go] bfs + dfs

> Author: Benhao
> Date: 2022-03-22
> Upvotes: 58
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Consider a prefix tree.
Lexicographic order gives the following structure:
With root (prefix) 1, its children are 10-19, all sharing prefix 1.
With root 10, its children are 100-109, all sharing prefix 10.
And so on

Find which root and descendant contain the kth number.
If the entire subtree rooted at 1 is too small, move across to root 2 and continue searching.

### Code

```Python3 []
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # How many numbers at most n start with 1?
        # 1 10-19 100-199 1000-1999 = 1111
        def dfs(l, r):
            # This level contains r - l + 1 available nodes; recurse to the next level
            # l * 10 changes 10 to 100; r * 10 + 9 changes 19 to 199
            return 0 if l > n else min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)
        
        cur = 1
        k -= 1
        while k:
            cnts = dfs(cur, cur)
            # If the entire subtree contains fewer nodes than needed, skip it and move to the next node at this level (for example, 1 -> 2)
            if cnts <= k:
                k -= cnts
                cur += 1
            # The answer is among the current node's descendants; consume the root and descend with DFS (for example, 1 -> 10)
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
