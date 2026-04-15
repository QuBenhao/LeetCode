# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-10-02
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
L可以向左移动，R可以向右移动，但是L不能跨过R，R也不能跨过L。
我们遍历维护L和R的情况，当出现以下情形之一，即可返回否:
1. 当前目标需要一个R而原字符串遇到了L，怎么也搞不出这个R了
2. 当前目标需要一个L而原字符串遇到了R，怎么也搞不出这个L了

### 代码

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