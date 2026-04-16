# [Python/Java] 26进制转换为10进制

> Author: Benhao
> Date: 2021-07-29
> Upvotes: 4
> Tags: Java, Python, Python3

---

```python3 []
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cur = 0
        for c in columnTitle:
            cur = 26 * cur + ord(c) - ord('A') + 1
        return cur
```
```java []
class Solution {
    public int titleToNumber(String columnTitle) {
        char[] chars = columnTitle.toCharArray();
        int ans = 0;
        for(char c: chars)
            ans = 26 * ans + (c - 'A' + 1);
        return ans;
    }
}
```
