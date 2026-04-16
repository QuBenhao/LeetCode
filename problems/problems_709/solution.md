# [Python/Java/JavaScript] bravo

> Author: Benhao
> Date: 2021-12-12
> Upvotes: 14
> Tags: Go, Java, JavaScript, PHP, Python

---

使用内置函数全部一行
```python3 []
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
```
```Java []
class Solution {
    public String toLowerCase(String s) {
        return s.toLowerCase();
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    return s.toLowerCase()
};
```
```Go []
func toLowerCase(s string) string {
    return strings.ToLower(s)
}
```

不使用内置函数
```python3 []
class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(c) - ord('A') + ord('a')) if 'A' <= c <= 'Z' else c for c in s])
```
```Java []
class Solution {
    public String toLowerCase(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c <= 'Z' && c >= 'A')
                sb.append((char)('a' + c - 'A'));
            else
                sb.append(c);
        }
        return sb.toString();
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
const a = 'a'.charCodeAt(), A = 'A'.charCodeAt(), Z = 'Z'.charCodeAt()
var toLowerCase = function(s) {
    const ans = []
    for(let i=0;i<s.length;i++){
        if(s.charCodeAt(i) >= A && s.charCodeAt(i) <= Z)
            ans.push(String.fromCharCode(a + s.charCodeAt(i) - A))
        else
            ans.push(s.charAt(i))
    }
    return ans.join("")
};
```
```Go []
func toLowerCase(s string) string {
    byteSlice := make([]byte, len(s))
    for i, r := range s {
        if r >= 'A' && r <= 'Z' {
            byteSlice[i] = byte('a') + s[i] - byte('A')
        } else {
            byteSlice[i] = s[i]
        }
    }
    return string(byteSlice)
}
```