# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-by-himymben-nrem
> date: 2022-08-10
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Reformat The String (reformat-the-string)
> url: https://leetcode.cn/problems/reformat-the-string/solutions/IryBBA/pythonjavatypescriptgo-by-himymben-nrem/

---
### 解题思路
先将原字符串分为字母和数字统计，然后根据题目要求返回答案

### 代码

```Python3 []
class Solution:
    def reformat(self, s: str) -> str:
        alphas, digits, n = [], [], len(s)
        for i, c in enumerate(s):
            if c.isdigit():
                digits.append(c)
            else:
                alphas.append(c)
            # 以下几种判断方式都可以
            #if 2 * max(len(digits), len(alphas)) > n + 1:
            #if min(len(alphas), len(digits)) + n - i < max(len(alphas), len(digits)):
            if abs(len(digits) - len(alphas)) + i > n:
                return ""
        ans, last_alpha = [], False 
        while alphas or digits:
            m, last_alpha = (alphas, True) if not last_alpha and len(alphas) >= len(digits) else (digits, False)
            ans.append(m.pop())
        return "".join(ans)
```
```Java []
class Solution {
    public String reformat(String s) {
        Deque<Character> digits = new ArrayDeque<>(), alphas = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < 'A') {
                digits.addLast(s.charAt(i));
            } else {
                alphas.addLast(s.charAt(i));
            }
            if (2 * Math.max(digits.size(), alphas.size()) > s.length() + 1) {
                return "";
            }
        }
        StringBuilder sb = new StringBuilder();
        boolean lastAlpha = false;
        while (!digits.isEmpty() || !alphas.isEmpty()) {
            Deque<Character> cur;
            if (!lastAlpha && alphas.size() >= digits.size()) {
                cur = alphas;
                lastAlpha = true;
            } else {
                cur = digits;
                lastAlpha = false;
            }
            sb.append(cur.removeFirst());
        }
        return sb.toString();
    }
}
```
```TypeScript []
const A = "A".charCodeAt(0)
function reformat(s: string): string {
    const digits: Array<string> = new Array<string>(), alphas: Array<string> = new Array<string>(), n = s.length
    for (let i = 0; i < n; i++) {
        if(s.charCodeAt(i) < A) {
            digits.push(s.charAt(i))
        } else {
            alphas.push(s.charAt(i))
        }
        if (Math.max(digits.length, alphas.length) * 2 > n + 1) {
            return ""
        }
    }
    const ans: Array<string> = new Array<string>()
    let lastAlpha = false
    while (digits.length > 0 || alphas.length > 0) {
        let cur: Array<string>
        if (!lastAlpha && alphas.length >= digits.length) {
            cur = alphas
            lastAlpha = true
        } else {
            cur = digits
            lastAlpha = false
        }
        ans.push(cur.pop())
    }
    return ans.join("")
};
```
```Go []
func reformat(s string) string {
    alphas, digits := []byte{}, []byte{}
    for i, n := 0, len(s); i < n; i++ {
        if s[i] < 'A' {
            digits = append(digits, s[i])
        } else {
            alphas = append(alphas, s[i])
        }
        if max(len(alphas), len(digits)) * 2 > n + 1 {
            return ""
        }
    }
    ans, last_alpha := []byte{}, false
    for len(alphas) > 0 || len(digits) > 0 {
        if !last_alpha && len(alphas) >= len(digits) {
            ans = append(ans, alphas[len(alphas) - 1])
            alphas = alphas[:len(alphas) - 1]
            last_alpha = true
        } else {
            ans = append(ans, digits[len(digits) - 1])
            digits = digits[:len(digits) - 1]
            last_alpha = false
        }
    }
    return string(ans)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```