# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-10-11
> Upvotes: 10
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按题意模拟即可

### 代码

```Python3
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return not (cnts := sum(c1 != c2 for c1, c2 in zip(s1, s2))) or (Counter(s1) == Counter(s2) and cnts == 2)
```
```Python3 []
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return not (diffs := [i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]) or (len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])
```
```Java []
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int a = -1, b = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (a == -1) {
                    a = i;
                } else if (b == -1) {
                    b = i;
                } else {
                    return false;
                }
            }
        }
        if (a != -1 && b == -1) {
            return false;
        }
        return a == -1 || (s1.charAt(a) == s2.charAt(b) && s1.charAt(b) == s2.charAt(a));
    }
}
```
```TypeScript []
function areAlmostEqual(s1: string, s2: string): boolean {
    let a: number = -1, b: number = -1
    for (let i = 0; i < s1.length; i++) {
        if (s1.charCodeAt(i) != s2.charCodeAt(i)) {
            if (a == -1) {
                a = i
            } else if (b == -1) {
                b = i
            } else {
                return false
            }
        }
    }
    if (a != -1 && b == -1) {
        return false
    }
    return a == -1 || (s1.charCodeAt(a) == s2.charCodeAt(b) && s1.charCodeAt(b) == s2.charCodeAt(a))
};
```
```Go []
func areAlmostEqual(s1 string, s2 string) bool {
    a, b := -1, -1
    for i := 0; i < len(s1); i++ {
        if s1[i] != s2[i] {
            if a == -1 {
                a = i
            } else if b == -1 {
                b = i
            } else {
                return false
            }
        }
    }
    return a == -1 || (b != -1 && s1[a] == s2[b] && s1[b] == s2[a])
}
```