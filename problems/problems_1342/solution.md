# [Python/Java/JavaScript/Go] See the underlying pattern: binary representation

> Author: Benhao
> Date: 2022-01-30
> Upvotes: 81
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach

[Happy Lunar New Year's Eve, everyone!]

For an odd number, subtract 1 and divide by 2; for an even number, divide by 2. Both are essentially a binary right shift, but odd numbers require an extra step.
An odd number occurs when `num & 1 == 1` after some right shifts, meaning that the corresponding bit was 1 before shifting.
An even number occurs when `num & 1 == 0` after some right shifts, meaning that the corresponding bit was 0 before shifting.
Thus, each binary `1` costs two steps, and each binary `0` costs one step.
The exception is the leftmost `1`: subtracting 1 makes it 0 without another division, so it costs one step.

For example:
22 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1 -> 0
10110 -> 1011 -> 1010 -> 101 -> 100 -> 10 -> 1 -> 0

Here is another algorithm for counting binary 1s: [Hamming Weight](https://www.cnblogs.com/yongssu/p/4348479.html).

### Code

```Python3 []
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(b:=bin(num)[2:]) + b.count('1') - 1
```
```Java []
class Solution {
    public int numberOfSteps(int num) {
        return num > 0 ? (int)(Math.log(num)/Math.log(2)) + bitCount(num) : num;
    }

    private int bitCount(int n) {
        n = n - ((n >>> 1) & 0x55555555);
        n = (n & 0x33333333) + ((n >>> 2) & 0x33333333);
        n = (n + (n >>> 4)) & 0x0F0F0F0F;
        return (n * 0x01010101) >>> 24;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    if(num == 0)
        return 0
    let n = num
    n = n - ((n >>> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >>> 2) & 0x33333333)
    n = (n + (n >>> 4)) & 0x0F0F0F0F
    return ((n * 0x01010101) >>> 24) + Math.floor(Math.log2(num))
};
```
```Go []
func numberOfSteps(num int) int {
    if num == 0 {
        return num
    }
    return bitCount(uint32(num)) + int(math.Floor(math.Log2(float64(num))))
}

func bitCount(n uint32) int {
    n = n - ((n >> 1) & 0x55555555);
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
    n = (n + (n >> 4)) & 0x0F0F0F0F;
    return int((n * 0x01010101) >> 24);
}
```
