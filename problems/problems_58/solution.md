# [Python/Go/C] 模拟

> Author: Benhao
> Date: 2024-02-27
> Upvotes: 11
> Tags: C, Go, Java, Python3, TypeScript

---

### 解题思路
从后往前找第一个非空格直到再遇到空格结束

### 代码

```Python3 []
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for c in s[::-1]:
            if c == ' ':
                if ans:
                    break
                continue
            ans += 1 
        return ans
```
```Go []
func lengthOfLastWord(s string) (ans int) {
    for i := len(s) - 1; i >= 0; i-- {
        if s[i] == ' ' {
            if ans > 0 {
                break
            }
            continue
        }
        ans++
    }
    return
}
```
```C []
int lengthOfLastWord(char* s) {
    int ans = 0;
    for (int i = strlen(s) - 1; i >= 0; i--) {
        if (s[i] == ' ') {
            if (ans > 0) {
                break;
            }
            continue;
        }
        ans++;
    }
    return ans;
}
```