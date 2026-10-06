# [Python/Java/JavaScript/Go] Simulation

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
At each character boundary, a 1 starts a two-bit character and a 0 starts a one-bit character. Simulate the parsing from the beginning and check whether the penultimate bit is a 1 starting a two-bit character.

### Code

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
