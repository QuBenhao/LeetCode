# [Python/Java] Memoized search or advanced factorization recursion

> slug: pythonjava-ji-yi-hua-sou-suo-by-himymben-tx2s
> date: 2021-09-18
> tags: Java, Python, Python3
> question: 2 Keys Keyboard (2-keys-keyboard)
> url: https://leetcode.cn/problems/2-keys-keyboard/solutions/PJhAcJ/pythonjava-ji-yi-hua-sou-suo-by-himymben-tx2s/

---
### Approach
Each operation either copies everything or pastes the clipboard. Once all current characters have been copied, copying again is unnecessary; only pasting helps.
Add pruning: if the remaining count is not divisible by the number of characters pasted, the target cannot be reached.

Copying and pasting always works in multiples of some factor. However many times we paste, the initial factor still divides the result. In other words, `we can copy only at a prime factor of n`; copying at other times cannot produce the target.
Copy the largest proper factor of the target. The required number of copy/paste operations is the target divided by that factor, giving a recursive solution.

> Heading out now... I will return to the proof that recursing on the largest factor is optimal.

### Code

```python3
class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dfs(cur, paste):
            if cur == n:
                return 0
            elif cur > n:
                return inf
            if paste and (n - cur) % paste:
                return inf
            return min(dfs(cur, cur), dfs(cur + paste, paste)) + 1 if paste and paste != cur else (dfs(cur + paste, paste) + 1 if paste else dfs(cur, cur) + 1)
        return dfs(1, 0)
```

```Java []
class Solution {
    public int minSteps(int n) {
        if(n == 1)
            return 0;
        if(maxDivide(n) == n)
            return n;
        int d = maxDivide(n);
        return n/d + minSteps(d);
    }

    public int maxDivide(int n){
        for(int i=n/2;i>=2;i--)
            if(n%i == 0)
                return i;
        return n;
    }
}
```
```Python3 []
class Solution:
    def minSteps(self, n: int) -> int:
        return self.minSteps(d) + n//d if (n > 1 and (d:=self.maxDivide(n)) != n) else (n if n > 1 else 0)

    @lru_cache(None)
    def maxDivide(self, n):
        for i in range(n//2, 2, -1):
            if not n % i:
                return i
        return n
```
