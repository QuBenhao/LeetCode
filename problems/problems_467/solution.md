# [Python/Java/JavaScript/Go] Dynamic programming

> slug: pythonjavajavascriptgo-by-himymben-em9d
> date: 2022-05-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Unique Substrings in Wraparound String (unique-substrings-in-wraparound-string)
> url: https://leetcode.cn/problems/unique-substrings-in-wraparound-string/solutions/0PmOX9/pythonjavajavascriptgo-by-himymben-em9d/

---
### Approach
Since s is fixed, maintain the longest valid substring ending with each character. Its length counts all distinct substrings ending with that character, since every shorter one is a suffix of the longest.
Maintain the current longest length during traversal.
If the current character follows the previous one in s, meaning their ASCII-code difference modulo 26 is 1, extend the previous length.
Otherwise, start a new substring.

### Code

```Python3 []
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp, cur = [0] * 26, 1
        dp[ord(p[0]) - ord('a')] = 1
        for c1, c2 in pairwise(p):
            if not (ord(c2) - ord(c1) - 1) % 26:
                cur += 1
            else:
                cur = 1
            dp[idx] = max(dp[idx := ord(c2) - ord('a')], cur)
        return sum(dp)
```
```Java []
class Solution {
    public int findSubstringInWraproundString(String p) {
        int[] dp = new int[26];
        int cur = 1;
        dp[p.charAt(0) - 'a'] = 1;
        for(int i = 1; i < p.length(); i++) {
            if((p.charAt(i) - p.charAt(i - 1) + 25) % 26 == 0) {
                cur++;
            } else {
                cur = 1;
            }
            dp[p.charAt(i) - 'a'] = Math.max(dp[p.charAt(i) - 'a'], cur);
        }
        int ans = 0;
        for(int v: dp) {
            ans += v;
        }
        return ans;
    }
}
```
```TypeScript []
function findSubstringInWraproundString(p: string): number {
    const dp = new Array(26).fill(0)
    let cur = 1
    dp[p.charCodeAt(0) - 'a'.charCodeAt(0)] = 1
    for(let i = 1; i < p.length; i++) {
        if((p.charCodeAt(i) - p.charCodeAt(i - 1) + 25) % 26 == 0) {
            cur++
        } else {
            cur = 1
        }
        const idx = p.charCodeAt(i) - 'a'.charCodeAt(0)
        dp[idx] = Math.max(dp[idx], cur)
    }
    return dp.reduce((a, b) => a + b)
};
```
```Go []
func findSubstringInWraproundString(p string) (ans int) {
    dp, cur := make([]int, 26), 1
    dp[p[0] - 'a'] = 1
    for i := 1; i < len(p); i++ {
        if (p[i] - p[i - 1] + 25) % 26 == 0 {
            cur++
        } else {
            cur = 1
        }
        if idx := p[i] - 'a'; dp[idx] < cur {
            dp[idx] = cur
        }
    }
    for _, v := range dp {
        ans += v
    }
    return
}
```
