# [Python/Java/JavaScript/Go] Greedy

> Author: Benhao
> Date: 2022-03-05
> Upvotes: 9
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
1. A longer sequence cannot be a subsequence of a shorter sequence.
2. Two sequences of equal length cannot be subsequences of each other if any character differs.


### Code

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
