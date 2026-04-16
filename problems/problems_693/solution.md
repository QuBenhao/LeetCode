# [Python/Java/JavaScript/Go] 位运算

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 28
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
题目要求n的二进制为101010交替，那么n和n右移一位刚好错开，它们异或的结果所有位都会是1。如果n有任意位有连续的1时，右移异或都会出现某位0。

如何快速判断全部为是1？其实就是判断是否异或结果为2的幂次减一。
判断2的幂次$a$的位运算方法为a&(a-1)==0

### 代码

```Python3 []
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not (a := n ^ (n >> 1)) & (a + 1)
```
```Java []
class Solution {
    public boolean hasAlternatingBits(int n) {
        int a = n ^ (n >> 1);
        return (a & (a + 1)) == 0;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    const a = n ^ (n >> 1)
    return (a & (a + 1)) === 0
};
```
```Go []
func hasAlternatingBits(n int) bool {
    a := n ^ (n >> 1)
    return a & (a + 1) == 0
}
```