# [Python/Java/JavaScript/Go] 分治思想

> Author: Benhao
> Date: 2022-02-01
> Upvotes: 102
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
将原问题拆解成子问题，如果某个字符在当前字符串中没有它对应的大写或小写字符，它必不能构成答案中的一部分，答案只能在它左边或在它右边。
我们返回该点左边或右边更长的答案即为答案。
如果不存在这样的字符，说明原字符串本身就是美好字符串。

### 代码

```Python3 []
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        for i, c in enumerate(s):
            # 存在任意不满足题目的割点
            if c.upper() not in s or c.lower() not in s:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key = len)
        return s
```
```Java []
class Solution {
    public String longestNiceSubstring(String s) {
        if(s.length() < 2)
            return "";
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if((c <= 'Z' && !s.contains(String.valueOf((char)((int)c + 32)))) || (c >= 'a' && !s.contains(String.valueOf((char)((int)c - 32))))){
                String s1 = longestNiceSubstring(s.substring(0, i)), s2 = longestNiceSubstring(s.substring(i+1));
                if(s1.length() >= s2.length())
                    return s1;
                return s2;
            }
        }
        return s;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function(s) {
    if(s.length < 2)
        return ""
    for(let i = 0; i < s.length; i++){
        const c = s.charCodeAt(i)
        if((c < 97 && s.indexOf(String.fromCharCode(c + 32))==-1) || (c >= 97 && s.indexOf(String.fromCharCode(c - 32))==-1)){
            const s1 = longestNiceSubstring(s.substring(0, i)), s2 = longestNiceSubstring(s.substring(i+1))
            if(s1.length >= s2.length)
                return s1
            return s2
        }
    }
    return s
};
```
```Go []
func longestNiceSubstring(s string) string {
    if len(s) < 2 {
        return ""
    }
    for i := 0; i < len(s); i++ {
        if (s[i] < 97 && !strings.Contains(s, string(s[i] + 32))) || (s[i] >= 97 && !strings.Contains(s, string(s[i] - 32))) {
            s1, s2 := longestNiceSubstring(s[:i]), longestNiceSubstring(s[i+1:])
            if len(s1) >= len(s2) {
                return s1
            }
            return s2
        }
    }
    return s
}
```