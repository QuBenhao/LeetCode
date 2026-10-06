# [Python/Go/C] Simulation

> Author: Benhao
> Date: 2024-02-27
> Upvotes: 11
> Tags: C, Go, Java, Python3, TypeScript

---

### Approach
Scan backward to the first non-space character, then continue until another space is reached.

### Code

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
