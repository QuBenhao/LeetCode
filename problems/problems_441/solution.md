# [Python/Java/JavaScript] Binary search

> slug: pythonjavajavascript-er-fen-by-himymben-8ebg
> date: 2021-10-10
> tags: Java, JavaScript, Python, Python3
> question: Arranging Coins (arranging-coins)
> url: https://leetcode.cn/problems/arranging-coins/solutions/TFpNLG/pythonjavajavascript-er-fen-by-himymben-8ebg/

---
### Approach
The problem asks for the largest positive integer $x$ satisfying $x^2 + x - 2*n \leq 0$, derived from the sum $\sum_{i=1}^x i$. The largest root can be found mathematically.
Alternatively, use binary search to find this largest positive integer.

### Code

```Python3 []
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i * (i+1) <= 2 * n
        l, r = 1, n
        n *= 2
        while l < r:
            mid = (l + r + 1) // 2
            s = mid * (mid + 1)
            if s == n:
                return mid
            elif s > n:
                r = mid - 1
            else:
                l = mid
        return l
```
```Java []
class Solution {
    public int arrangeCoins(int n) {
        int l = 1, r = n;
        while(l < r){
            int mid = (r - l + 1)/2 + l;
            long res = (long)mid * (mid + 1)/2;
            if(res == n)
                return mid;
            else if(res < n)
                l = mid;
            else
                r = mid - 1;
        }
        return l;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    let l = 1, r = n, mid, s;
    n *= 2;
    while (l < r){
        mid = Math.floor((l + r + 1) / 2);
        s = mid * (mid + 1);
        if (s == n)
            return mid;
        else if (s < n)
            l = mid;
        else
            r = mid - 1;
    }
    return l;
};
```
