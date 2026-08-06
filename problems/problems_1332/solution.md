# [Python/Java/JavaScript/Go] 回文判断

> slug: pythonjavajavascriptgo-hui-wen-pan-duan-v3gnj
> date: 2022-01-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Remove Palindromic Subsequences (remove-palindromic-subsequences)
> url: https://leetcode.cn/problems/remove-palindromic-subsequences/solutions/xHe7tp/pythonjavajavascriptgo-hui-wen-pan-duan-v3gnj/

---
### 解题思路
因为只有'a','b'两个字母且可以删除回文子序列，所以不管怎么样都可以把所有的'a'凑成一个序列，‘b’凑成另一个序列，他们都是回文的可以被删除，故最多需要两次。
所以只需要看本身是不是回文，可不可以一次删除即可。

### 代码

```Python3 []
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return (s != s[::-1]) + 1
```
```Java []
class Solution {
    public int removePalindromeSub(String s) {
        int n = s.length();
        for(int i=0;i<n/2;i++)
            if(s.charAt(i) != s.charAt(n-1-i))
                return 2;
        return 1;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    const n = s.length
    for(let i = 0; i < n - i; i++)
        if(s.charCodeAt(i) !== s.charCodeAt(n - 1 - i))
            return 2
    return 1
};
```
```Golang []
func removePalindromeSub(s string) int {
    for i, n := 0, len(s); i < n / 2; i++ {
        if s[i] != s[n - 1 - i]{
            return 2
        }
    }
    return 1
}
```