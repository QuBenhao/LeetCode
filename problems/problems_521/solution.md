# [Python/Java/JavaScript/Go] 贪心

> Author: Benhao
> Date: 2022-03-05
> Upvotes: 9
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
1. 一个长的序列一定不是一个短的序列的子序列
2. 相同长度的序列只要有一个字符不同就不是子序列


### 代码

```Python3 []
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
```
```Java []
class Solution {
    public int findLUSlength(String a, String b) {
        return a.equals(b) ? -1 : Math.max(a.length(), b.length());
    }
}
```
```JavaScript []
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var findLUSlength = function(a, b) {
    return a === b ? -1 : Math.max(a.length, b.length)
};
```
```Go []
func findLUSlength(a string, b string) int {
    if a == b {
        return -1
    } else if len(a) > len(b) {
        return len(a)
    } else {
        return len(b)
    }
}
```