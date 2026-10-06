# [Python/Java/TypeScript/Go] Matching parentheses

> slug: pythonjavatypescriptgo-cheng-dui-de-gua-bbsjz
> date: 2022-10-04
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Minimum Add to Make Parentheses Valid (minimum-add-to-make-parentheses-valid)
> url: https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/solutions/7NT8yT/pythonjavatypescriptgo-cheng-dui-de-gua-bbsjz/

---
### Approach
Each closing parenthesis cancels an earlier opening parenthesis. If none is available, this closing parenthesis is unmatched and needs an opening parenthesis added.
Any opening parentheses left over also need matching closing parentheses added.

### Code

```Python3 []
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans, left = 0, 0
        for c in s:
            if c == '(':
                left += 1
            else:
                left -= 1
            if left < 0:
                ans += 1
                left = 0
        return left + ans
```
```Java []
class Solution {
    public int minAddToMakeValid(String s) {
        int ans = 0, left = 0;
        for (int i = 0; i < s.length(); i++) {
            left += s.charAt(i) == '(' ? 1 : -1;
            if (left < 0) {
                ans++;
                left++;
            }
        }
        return ans + left;
    }
}
```
```TypeScript []
function minAddToMakeValid(s: string): number {
    let ans: number = 0, left: number = 0
    for (const c of s) {
        left += c === "(" ? 1 : -1
        if (left < 0) {
            ans++
            left++
        }
    }
    return ans + left
};
```
```Go []
func minAddToMakeValid(s string) (ans int) {
    left := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            left++
        } else {
            left--
        }
        if left < 0 {
            left++
            ans++
        }
    }
    return ans + left
}
```
```C++ []
class Solution {
public:
    int minAddToMakeValid(string s) {
        int ans = 0, left = 0;
        for (auto &c: s) {
            if (c == '(') {
                left++;
            } else {
                left--;
            }
            if (left < 0) {
                ans++;
                left++;
            }
        }
        return ans + left;
    }
};
```
