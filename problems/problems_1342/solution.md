# [Python/Java/JavaScript/Go] 透过现象看本质 - 二进制

> Author: Benhao
> Date: 2022-01-30
> Upvotes: 81
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路

【除夕快乐家人们】

遇到奇数减一除二、遇到偶数除二，本质上都是二进制的右移，只是奇数需要额外的一步。
出现奇数其实是在右移一定次数后，`num & 1 == 1`，也就是右移前该位为1。
出现偶数其实是在右移一定次数后，`num & 1 == 0`, 也就是右移前该位为0。
也就是说，每个二进制位的`1`都会带来两步的代价，每个二进制位的`0`都会带来一步的代价。
唯一特殊的是二进制最左的`1`最后减一为0不需要除二了，所以步数为1。

举个例子：
22 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1 -> 0
10110 -> 1011 -> 1010 -> 101 -> 100 -> 10 -> 1 -> 0

另外分享一个计算二进制1的个数的算法：[Hamming Weight](https://www.cnblogs.com/yongssu/p/4348479.html)

### 代码

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