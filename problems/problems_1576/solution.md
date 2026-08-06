# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-96qi
> date: 2022-01-04
> tags: Go, Java, JavaScript, Python, Python3
> question: Replace All ?'s to Avoid Consecutive Repeating Characters (replace-all-s-to-avoid-consecutive-repeating-characters)
> url: https://leetcode.cn/problems/replace-all-s-to-avoid-consecutive-repeating-characters/solutions/YL2tWC/pythonjavajavascriptgo-mo-ni-by-himymben-96qi/

---
### 解题思路
每次填入与两边不相同的字母即可

### 代码

```Python3 []
class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i] == "?":
                for j in range(26):
                    ch = ord('a') + j
                    if ans and ch == ord(ans[-1]):
                        continue
                    if i < len(s) - 1 and ch == ord(s[i+1]):
                        continue
                    ans.append(chr(ch))
                    break
            else:
                ans.append(s[i])
        return "".join(ans)
```
```Java []
class Solution {
    public String modifyString(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<s.length();i++)
            if(s.charAt(i) == '?'){
                for(int j=0;j<26;j++){
                    if(sb.length() > 0 && 'a' + j == sb.charAt(sb.length() - 1))
                        continue;
                    if(i < s.length() - 1 && 'a' + j == s.charAt(i+1))
                        continue;
                    sb.append((char)('a' + j));
                    break;
                }
            }else
                sb.append(s.charAt(i));
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    const ans = new Array()
    for(let i=0;i<s.length;i++)
        if(s.charAt(i) == '?'){
            for(let j=0;j<26;j++){
                if(ans.length > 0 && ans[ans.length - 1].charCodeAt(0) == 'a'.charCodeAt(0) + j)
                    continue;
                if(i < s.length - 1 && s.charCodeAt(i+1) == 'a'.charCodeAt(0) + j)
                    continue;
                ans.push(String.fromCharCode('a'.charCodeAt(0) + j))
                break
            }
        }else
            ans.push(s.charAt(i))
    return ans.join("")
};
```
```Go []
func modifyString(s string) string {
    ans := make([]rune, len(s))
    for i, r := range s {
        if s[i] == byte('?') {
            for j := 0; j < 26; j++ {
                b := rune('a' + j)
                if i > 0 && ans[i - 1] == b {
                    continue
                }
                if i < len(s) - 1 && rune(s[i + 1]) == b{
                    continue
                }
                ans[i] = b
                break
            }
        }else{
            ans[i] = r
        }
    }
    return string(ans)
}
```