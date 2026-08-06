# [Python/Java/JavaScript/Go] 双指针扫描

> slug: pythonjavajavascriptgo-shuang-zhi-zhen-s-1zjg
> date: 2021-11-30
> tags: Go, Java, JavaScript, Python, Python3
> question: Consecutive Characters (consecutive-characters)
> url: https://leetcode.cn/problems/consecutive-characters/solutions/F0Rif8/pythonjavajavascriptgo-shuang-zhi-zhen-s-1zjg/

---
```python3 []
class Solution:
    def maxPower(self, s: str) -> int:
        l = r = ans = 0
        while l < len(s):
            while r < len(s) and s[r] == s[l]:
                r += 1
            ans = max(ans, r - l)
            l = r
        return ans
```
```Java []
class Solution {
    public int maxPower(String s) {
        int ans = 0;
        for(int l=0,r=0;l<s.length();){
            while(r<s.length()&&s.charAt(r) == s.charAt(l)){
                r++;
            }
            ans = Math.max(ans, r - l);
            l = r;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
    let ans = 0
    for(let i=0,j=0;i<s.length;){
        while(j<s.length&&s.charAt(j)==s.charAt(i))
            j++
        ans = Math.max(ans, j - i)
        i = j
    }
    return ans
};
```
```Go []
func maxPower(s string) (ans int) {
    for l,r := 0,0; l < len(s); l = r {
        for ;r < len(s) && s[r] == s[l]; r++ {}
        if v := r - l; v > ans {
            ans = v
        }
    }
    return ans
}
```
```python3
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(obj)) for _, obj in groupby(s))
```