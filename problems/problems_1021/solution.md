# [Python/Java/TypeScript/Go] 双指针

> slug: pythonjavatypescriptgo-shuang-zhi-zhen-b-ix9d
> date: 2022-05-28
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Remove Outermost Parentheses (remove-outermost-parentheses)
> url: https://leetcode.cn/problems/remove-outermost-parentheses/solutions/3WFprE/pythonjavatypescriptgo-shuang-zhi-zhen-b-ix9d/

---
### 解题思路
根据左右括号的平衡，找每个使得左右括号数量一致的点，去掉这些点即可。

### 代码

```Python3 []
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = j = cur = 0
        ans = ""
        while i < len(s):
            cur += 1
            j += 1
            while j < len(s) and cur:
                cur += 1 if s[j] == '(' else -1
                j += 1
            ans += s[i + 1:j - 1]
            i = j
        return ans
```
```Java []
class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0, j = 0, cur = 0, n = s.length(); i < n; i = j) {
            j++;
            cur++;
            while(j < n && cur > 0) {
                cur += s.charAt(j) == '(' ? 1 : -1;
                j++;
            }
            sb.append(s.substring(i + 1, j - 1));
        }
        return sb.toString();
    }
}
```
```TypeScript []
function removeOuterParentheses(s: string): string {
    const ans = new Array(), n = s.length
    for(let i = 0, j = 0, cur = 0; i < n; i = j) {
        j++
        cur++
        while(j < n && cur > 0) {
            cur += s.charCodeAt(j) == '('.charCodeAt(0) ? 1 : -1
            j++
        }
        ans.push(s.substring(i + 1, j - 1))
    }
    return ans.join('')
};
```
```Go []
func removeOuterParentheses(s string) string {
    ans, n := []byte{}, len(s)
    for i, j, cur := 0, 0, 0; i < n; i = j {
        j++
        cur++
        for j < n && cur > 0 {
            if s[j] == '(' {
                cur++
            } else {
                cur--
            }
            ans = append(ans, s[j])
            j++
        }
        ans = ans[:len(ans)-1]
    }
    return string(ans)
}
```