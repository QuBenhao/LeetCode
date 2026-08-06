# [Python/Java/JavaScript/Go] 动态规划

> slug: pythonjavajavascriptgo-by-himymben-em9d
> date: 2022-05-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Unique Substrings in Wraparound String (unique-substrings-in-wraparound-string)
> url: https://leetcode.cn/problems/unique-substrings-in-wraparound-string/solutions/0PmOX9/pythonjavajavascriptgo-by-himymben-em9d/

---
### 解题思路
因为s是一个固定的字符串，我们维护以每个字符结尾的最长子串长度，就可以直接累加所有以该字符结尾的子字符串 (每个字符统计最长长度即可。因为更小的长度都是更长的长度的子串)。
在遍历的时候我们维护一个当前的最长长度。
如果当前字符满足与上一个字符在s中连续（也就是后面的比前面的ASCII的差模26大1），那么以当前字符结尾的最长长度就从前面累加，
否则就是新的开始。

### 代码

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