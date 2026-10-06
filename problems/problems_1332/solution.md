# [Python/Java/JavaScript/Go] Palindrome check

> slug: pythonjavajavascriptgo-hui-wen-pan-duan-v3gnj
> date: 2022-01-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Remove Palindromic Subsequences (remove-palindromic-subsequences)
> url: https://leetcode.cn/problems/remove-palindromic-subsequences/solutions/xHe7tp/pythonjavajavascriptgo-hui-wen-pan-duan-v3gnj/

---
### Approach
Only 'a' and 'b' occur, and palindromic subsequences can be removed. All 'a' characters form one subsequence and all 'b' characters another; both are palindromes, so at most two removals are needed.
We only need to check whether the string itself is a palindrome and can be removed in one step.

### Code

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
