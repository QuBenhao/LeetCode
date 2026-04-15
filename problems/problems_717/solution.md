# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
每次第一次遇到一个1，它必然是一个2比特字符；而第一次遇到一个0，它必然是一个1比特字符，从头开始模拟比特分割，看最终倒数第二个点是否为一个2比特字符开头的1

### 代码

```Python3 []
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1 or bits[-2] == 0:
            return True
        idx = 0
        while idx < len(bits) - 2:
            idx += bits[idx] + 1
        return idx == len(bits) - 1
```
```Java []
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int n = bits.length;
        if(n == 1 || bits[n - 2] == 0)
            return true;
        int idx = 0;
        while(idx < n - 2)
            idx += bits[idx] + 1;
        return idx == n - 1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    const n = bits.length
    if(n == 1 || bits[n - 2] == 0)
        return true
    let idx = 0
    while(idx < n - 2)
        idx += bits[idx] + 1
    return idx == n - 1
};
```
```Go []
func isOneBitCharacter(bits []int) bool {
    n := len(bits)
    if n == 1 || bits[n - 2] == 0 {
        return true
    }
    idx := 0
    for idx < n - 2 {
        idx += bits[idx] + 1
    }
    return idx == n - 1
}
```