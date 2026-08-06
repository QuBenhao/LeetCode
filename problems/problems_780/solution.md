# [Python/Java/JavaScript/Go] 逆向思维 - 辗转相除

> slug: pythonjavajavascriptgo-zhan-zhuan-xiang-eh8p0
> date: 2022-04-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Reaching Points (reaching-points)
> url: https://leetcode.cn/problems/reaching-points/solutions/wB7Jda/pythonjavajavascriptgo-zhan-zhuan-xiang-eh8p0/

---
### 解题思路
tx比sx大、ty比sy大，说明我们还要发生加法，那么tx和ty中的大一点的数，就一定是由小一点的数加了k次得到，我们可以直接取余。
为什么取余而不是减法，这样错过了起始值也没关系？因为另一个数还比起始值大，它肯定需要从小的数加出来。而对方上一次比它小的数就是和它的余数。

我们最终判断是否有一个相等且另一个和起始值的差是另一个起始值的整数倍即可。

### 代码

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