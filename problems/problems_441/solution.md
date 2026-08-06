# [Python/Java/JavaScript] 二分

> slug: pythonjavajavascript-er-fen-by-himymben-8ebg
> date: 2021-10-10
> tags: Java, JavaScript, Python, Python3
> question: Arranging Coins (arranging-coins)
> url: https://leetcode.cn/problems/arranging-coins/solutions/TFpNLG/pythonjavajavascript-er-fen-by-himymben-8ebg/

---
### 解题思路
题目其实是找最大的正整数$x$，使得$x^2 + x - 2*n \leq 0$ (由求和公式$\sum_{i=1}^x i$推出)。根据这个方程可以用数学得到最大的根。
避免数学的话我们可以用二分，去找到这个最大的正整数即可。

### 代码

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