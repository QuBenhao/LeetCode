# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-epc3
> date: 2022-09-29
> tags: C++, Go, Java, JavaScript, Python, Python3, TypeScript
> question: String Rotation LCCI (string-rotation-lcci)
> url: https://leetcode.cn/problems/string-rotation-lcci/solutions/LyiwE7/pythonjavatypescriptgo-mo-ni-by-himymben-epc3/

---
### 解题思路
所有带旋转字眼的，把原数组复制一倍解决

### 代码

```Python3 []
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in (s1 + s1)
```
```Java []
class Solution {
    public boolean isFlipedString(String s1, String s2) {
        return s1.length() == s2.length() && (s1 + s1).indexOf(s2) != -1;
    }
}
```
```TypeScript []
function isFlipedString(s1: string, s2: string): boolean {
    return s1.length == s2.length && (s1 + s1).indexOf(s2) != -1
};
```
```Go []
func isFlipedString(s1 string, s2 string) bool {
    return len(s1) == len(s2) && strings.Index(s1 + s1, s2) != -1
}
```
```C++ []
class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        return s1.length() == s2.length() && (s1 + s1).find(s2) != string::npos;
    }
};
```