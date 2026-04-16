# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-10-01
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按题意模拟即可

### 代码

```Python3 []
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.compile(r"[- ]").sub("", number)
        idx, n, ans = 0, len(number), []
        while idx + 4 < n:
            ans.append(number[idx:idx+3])
            idx += 3
        if n - idx == 4:
            ans.append(number[idx:idx+2])
            idx += 2
        ans.append(number[idx:n])
        return "-".join(ans)
```
```Java []
class Solution {
    public String reformatNumber(String number) {
        String s = number.replace("-", "").replace(" ", "");
        int idx = 0, n = s.length();
        StringBuilder sb = new StringBuilder();
        for (; idx < n - 4; idx += 3) {
            sb.append(s.substring(idx, idx + 3));
            sb.append("-");
        }
        if (n - idx == 4) {
            sb.append(s.substring(idx, idx + 2));
            idx += 2;
            sb.append("-");
        }
        sb.append(s.substring(idx, n));
        return sb.toString();
    }
}
```
```TypeScript []
function reformatNumber(number: string): string {
    const s: string = number.replace(/[- ]/g, ''), n: number = s.length, ans: Array<string> = new Array<string>()
    let idx: number = 0
    for (; idx < n - 4; idx += 3) {
        ans.push(s.substr(idx, 3))
    }
    if (idx == n - 4) {
        ans.push(s.substr(idx, 2))
        idx += 2
    }
    ans.push(s.substring(idx, n))
    return ans.join("-")
};
```
```Go []
func reformatNumber(number string) string {
    s := strings.ReplaceAll(strings.ReplaceAll(number, "-", ""), " ", "")
    idx, n, ans := 0, len(s), []string{}
    for ; idx < n - 4; idx += 3 {
        ans = append(ans, s[idx:idx+3])
    }
    if idx == n - 4 {
        ans = append(ans, s[idx:idx+2])
        idx += 2
    }
    ans = append(ans, s[idx:n])
    return strings.Join(ans, "-")
}
```