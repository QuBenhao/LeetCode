# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-05-11
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
该用户太懒了只有代码

### 代码

```Python3 []
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*strs))
```
```Java []
class Solution {
    public int minDeletionSize(String[] strs) {
        int ans = 0;
        out:
        for(int i = 0; i < strs[0].length(); i++) {
            for(int j = 1; j < strs.length; j++) {
                if(strs[j].charAt(i) < strs[j - 1].charAt(i)) {
                    ans++;
                    continue out;
                }
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    let ans = 0
    out:
    for(let i = 0; i < strs[0].length; i++) {
        for(let j = 1; j < strs.length; j++) {
            if(strs[j].charCodeAt(i) < strs[j - 1].charCodeAt(i)) {
                ans++
                continue out
            }
        }
    }
    return ans
};
```
```Go []
func minDeletionSize(strs []string) (ans int) {
    for i := 0; i < len(strs[0]); i++ {
        for j := 1; j < len(strs); j++ {
            if strs[j][i] < strs[j - 1][i] {
                ans++
                break
            }
        }
    }
    return
}
```