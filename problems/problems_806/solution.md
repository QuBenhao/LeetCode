# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-2wt8
> date: 2022-04-11
> tags: Go, Java, JavaScript, Python, Python3
> question: Number of Lines To Write String (number-of-lines-to-write-string)
> url: https://leetcode.cn/problems/number-of-lines-to-write-string/solutions/bKb483/pythonjavajavascriptgo-mo-ni-by-himymben-2wt8/

---
### 解题思路
每攒够超过一百就将多出的宽度新起一行

### 代码

```Python3 []
MAX_WIDTH = 100
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans, cur = 1, 0
        for c in s:
            width = widths[ord(c) - ord('a')]
            if cur + width > MAX_WIDTH:
                ans += 1
                cur = width
            else:
                cur += width
        return [ans, cur]
```
```Java []
class Solution {
    private static final int MAX_WIDTH = 100;
    public int[] numberOfLines(int[] widths, String s) {
        int ans = 1, cur = 0;
        for(int i = 0; i < s.length(); i++) {
            int width = widths[s.charAt(i) - 'a'];
            if(cur + width > MAX_WIDTH) {
                ans += 1;
                cur = width;
            } else
                cur += width;
        }
        return new int[]{ans, cur};
    }
}
```
```JavaScript []
const MAX_WIDTH = 100
/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function(widths, s) {
    let ans = 1, cur = 0
    for(let i = 0; i < s.length; i++) {
        const width = widths[s.charCodeAt(i) - 'a'.charCodeAt(0)]
        if(cur + width > MAX_WIDTH) {
            ans += 1
            cur = width
        } else
            cur += width
    }
    return [ans, cur]
};
```
```Go []
const maxWidth int = 100
func numberOfLines(widths []int, s string) []int {
    ans, cur := 1, 0
    for _, r := range s {
        if width := widths[r - 'a']; cur + width > maxWidth {
            ans++
            cur = width
        } else {
            cur += width
        }
    }
    return []int{ans, cur}
}
```