# [Python/Java/JavaScript/Go] 覆盖匹配只有两种情况

> slug: pythonjavajavascriptgo-fu-gai-pi-pei-zhi-7m38
> date: 2021-12-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Repeated String Match (repeated-string-match)
> url: https://leetcode.cn/problems/repeated-string-match/solutions/1PFsei/pythonjavajavascriptgo-fu-gai-pi-pei-zhi-7m38/

---
### 解题思路
覆盖$b$字符串至少需要$\lceil \frac{b}{a} \rceil$个$a$字符串，至多需要$\lceil \frac{b}{a} \rceil + 1$个$a$字符串。

### 代码

```Python3 []
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        return l if (a * (l:=ceil(len(b)/len(a)))).find(b) != -1 else l + 1 if (a * (l + 1)).find(b) != -1 else -1
```
```Java []
class Solution {
    public int repeatedStringMatch(String a, String b) {
        int l = (b.length() + a.length() - 1)/a.length();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<l;i++)
            sb.append(a);
        for(int i=0;i<=sb.length()-b.length();i++){
            if(sb.substring(i, i + b.length()).equals(b))
                return l;
        }
        sb.append(a);
        for(int i=a.length()*l-b.length()+1;i<=sb.length()-b.length();i++)
            if(sb.substring(i, i + b.length()).equals(b))
                return l+1;
        return -1;
    }
}
```
```JavaScript []
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    const l = Math.ceil(b.length/a.length)
    if(a.repeat(l).includes(b))
        return l
    if(a.repeat(l+1).includes(b))
        return l + 1
    return -1
};
```
```Go []
func repeatedStringMatch(a string, b string) int {
    l := (len(b) + len(a) - 1)/len(a)
    s := strings.Repeat(a, l)
    if strings.Contains(s, b) {
        return l
    }
    s += a
    if strings.Contains(s, b) {
        return l + 1
    }
    return -1
}
```