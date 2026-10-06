# [Python/Java/JavaScript/Go] Josephus problem

> Author: Benhao
> Date: 2022-05-03
> Upvotes: 73
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
A classic problem.

The first round removes person $k$, reducing the game to $n-1$ people.
Suppose $f(n-1,k)$ gives the index of the final survivor.
After removing person $k$, the game with $n-1$ people starts at the original person $k+1$.
The old and new indices therefore differ by $k$.
Using indices $0$ through $n-1$ avoids repeatedly handling the offset of 1; add 1 only at the end. The recurrence is:
$f(n,k) = (f(n - 1, k) + k) \% n$

With only one person left, that person survives.
Thus, $f(1,k) = 0$.
Starting from $f(1,k)$, derive $f(2,k)$ and continue through $f(n,k)$.

### Code

```Python3 []
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
```
```Java []
class Solution {
    public int findTheWinner(int n, int k) {
        int ans = 0;
        for(int i = 2; i <= n; i++)
            ans = (ans + k) % i;
        return ans + 1;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let ans = 0
    for(let i = 2; i <= n; i++)
        ans = (ans + k) % i
    return ans + 1
};
```
```Go []
func findTheWinner(n int, k int) (ans int) {
    for i := 2; i <= n; i++ {
        ans = (ans + k) % i
    }
    ans++
    return
}
```
