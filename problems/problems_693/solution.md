# [Python/Java/JavaScript/Go] Bitwise operations

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 28
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
The binary representation of n must alternate as 101010. Shifting n right by one offsets this pattern, so XORing the two gives all ones. If n has adjacent ones, at least one bit in the XOR result is zero.

How can we quickly check for all ones? Check whether the XOR result is one less than a power of two.
The bitwise test for a power of two $a$ is a&(a-1)==0.

### Code

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
