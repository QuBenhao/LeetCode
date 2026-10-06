# [Python/Java/JavaScript/Go] Difference-based counting

> Author: Benhao
> Date: 2022-01-06
> Upvotes: 35
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Add 1 for an opening parenthesis and subtract 1 for a closing parenthesis; track the maximum.

### Code

```Python3 []
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                ans = max(cur, ans)
            elif c == ')':
                cur -= 1
        return ans
```
```Java []
class Solution {
    public int maxDepth(String s) {
        int ans = 0;
        for(int i=0,cur=0;i<s.length();i++)
            if(s.charAt(i) == '('){
                cur++;
                ans = Math.max(ans, cur);
            } else if(s.charAt(i) == ')')
                cur--;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let ans = 0, cur = 0
    for(const c of s)
        if(c == '('){
            cur++
            ans = Math.max(cur, ans)
        } else if (c == ')')
            cur--
    return ans
};
```
```Go []
func maxDepth(s string) (ans int) {
    cur := 0
    for _, r := range s {
        if r == '('{
            cur++
            if cur > ans {
                ans = cur
            }
        } else if r == ')' {
            cur--
        }
    }
    return
}
```
