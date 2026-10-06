# [Python/Java/TypeScript/Go] Simulation

> Author: Benhao
> Date: 2022-10-03
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
There must be no 0 between the leftmost and rightmost 1.

### Code

```Python3 []
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "0" not in s[s.index("1"):len(s) - s[::-1].index("1")]
```
```Java []
class Solution {
    public boolean checkOnesSegment(String s) {
        return !s.substring(s.indexOf("1"), s.lastIndexOf("1")).contains("0");
    }
}
```
```TypeScript []
function checkOnesSegment(s: string): boolean {
    return !s.substring(s.indexOf("1"), s.lastIndexOf("1")).match("0")
};
```
```Go []
func checkOnesSegment(s string) bool {
    return strings.Index(s[strings.Index(s, "1"):strings.LastIndex(s, "1")], "0") == -1
}
```
