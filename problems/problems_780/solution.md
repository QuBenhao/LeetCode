# [Python/Java/JavaScript/Go] Work backward with the Euclidean algorithm

> slug: pythonjavajavascriptgo-zhan-zhuan-xiang-eh8p0
> date: 2022-04-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Reaching Points (reaching-points)
> url: https://leetcode.cn/problems/reaching-points/solutions/wB7Jda/pythonjavajavascriptgo-zhan-zhuan-xiang-eh8p0/

---
### Approach
If tx is greater than sx and ty is greater than sy, additions are still needed. The larger of tx and ty must have been obtained by adding the smaller value k times, so we can take the remainder directly.
Why can we use the remainder instead of subtraction without worrying about skipping the starting value? The other value is still larger than its starting value, so it must have been built by adding the smaller value. Its counterpart's last smaller value is precisely the remainder.

Finally, check whether one coordinate equals its starting value and the difference in the other coordinate is an integer multiple of the first starting value.

### Code

```Python3 []
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            tx, ty = (tx % ty, ty) if tx > ty else (tx, ty % tx)
        return (tx == sx and ty >= sy and not (ty - sy) % sx) or (ty == sy and tx >= sx and not(tx - sx) % sy)
```
```Java []
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while(tx > sx && ty > sy) {
            if(tx > ty)
                tx = tx % ty;
            else
                ty = ty % tx;
        }
        return (tx == sx && ty >= sy && (ty - sy) % sx == 0) || (ty == sy && (tx >= sx) && (tx -sx) % sy == 0);
    }
}
```
```JavaScript []
/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} tx
 * @param {number} ty
 * @return {boolean}
 */
var reachingPoints = function(sx, sy, tx, ty) {
    while(tx > sx && ty > sy) {
        if(tx > ty)
            tx %= ty
        else
            ty %= tx
    }
    return (tx == sx && ty >= sy && (ty - sy) % sx == 0) || (ty == sy && tx >= sx && (tx - sx) % sy == 0)
};
```
```Go []
func reachingPoints(sx int, sy int, tx int, ty int) bool {
    for tx > sx && ty > sy {
        if tx > ty {
            tx %= ty
        } else {
            ty %= tx
        }
    }
    return (tx == sx && ty >= sy && (ty - sy) % sx == 0) || (ty == sy && tx >= sx && (tx - sx) % sy == 0)
}
```
