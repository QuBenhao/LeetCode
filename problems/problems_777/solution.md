# [Python/Java/TypeScript/Go] Simulation

> Author: Benhao
> Date: 2022-10-02
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
L can move left and R can move right, but neither can cross the other.
Track L and R while scanning, and return false if either of these occurs:
1. The target currently needs an R but the original string encounters an L; that R can never be supplied
2. The target currently needs an L but the original string encounters an R; that L can never be supplied

### Code

```Python3 []
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        L, R = 0, 0
        for c1, c2 in zip(start, end):
            if (c1 == 'L' and R > 0) or (c1 == 'R' and L < 0):
                return False
            L += c1 == 'L'
            R += c1 == 'R'
            L -= c2 == 'L'
            R -= c2 == 'R'
            if (L != 0 and R != 0) or L > 0 or R < 0:
                return False
        return L == R == 0
```
```Java []
class Solution {
    public boolean canTransform(String start, String end) {
        int l = 0, r = 0;
        for (int i = 0, n = start.length(); i < n; i++) {
            if ((start.charAt(i) == 'L' && r > 0) || (start.charAt(i) == 'R' && l < 0)) {
                return false;
            }
            l += start.charAt(i) == 'L' ? 1 : 0;
            r += start.charAt(i) == 'R' ? 1 : 0;
            l -= end.charAt(i) == 'L' ? 1 : 0;
            r -= end.charAt(i) == 'R' ? 1 : 0;
            if ((l != 0 && r != 0) || l > 0 || r < 0) {
                return false;
            }
        }
        return l == r && l == 0;
    }
}
```
```TypeScript []
function canTransform(start: string, end: string): boolean {
    let l: number = 0, r: number = 0
    for (let i = 0, n = start.length; i < n; i++) {
        if ((start.charAt(i) == 'R' && l < 0) || (start.charAt(i) == 'L' && r > 0)) {
            return false
        }
        l += start.charAt(i) == 'L' ? 1 : 0
        r += start.charAt(i) == 'R' ? 1 : 0
        l -= end.charAt(i) == 'L' ? 1 : 0
        r -= end.charAt(i) == 'R' ? 1 : 0
        if ((l != 0 && r != 0) || l > 0 || r < 0) {
            return false
        }
    }
    return l == r && l == 0
};
```
```Go []
func canTransform(start string, end string) bool {
    l, r := 0, 0
    for i, n := 0, len(start); i < n; i++ {
        if (start[i] == 'R' && l < 0) || (start[i] == 'L' && r > 0) {
            return false
        }
        if start[i] == 'L' {
            l++
        } else if start[i] == 'R' {
            r++
        }
        if end[i] == 'L' {
            l--
        } else if end[i] == 'R' {
            r--
        }
        if (l != 0 && r != 0) || l > 0 || r < 0 {
            return false
        }
    }
    return l == r && l == 0
}
```
