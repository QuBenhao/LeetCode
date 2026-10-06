# [Python/Java/TypeScript/Go] Recursion

> Author: Benhao
> Date: 2022-08-07
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Inspired by [this excellent solution](https://leetcode.cn/problems/special-binary-string/solution/zhuan-huan-wei-gua-hao-zi-fu-chuan-jiu-hen-rong-yi/),
Treat 1 as an opening parenthesis and 0 as a closing parenthesis; this is essentially a valid-parentheses problem.
The goal is to place as many opening parentheses as possible at the front.

### Code

```Python3 []
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # cur: prefix sum; last: the end of the previous special sequence
        cur = last = 0
        # All available special subsequences
        candidates = []
        for i, c in enumerate(s):
            cur += 1 if c == '1' else -1
            # A special sequence must start with 1 and end with 0
            if not cur:
                # Maximize the current special sequence first; its fixed endpoints remain 1 and 0, so recurse on the interior
                candidates.append('1' + self.makeLargestSpecial(s[last + 1:i]) + '0')
                last = i + 1
        # Special subsequences can be swapped any number of times, so sort them in descending order and concatenate
        return "".join(sorted(candidates, reverse=True))
```
```Java []
class Solution {
    public String makeLargestSpecial(String s) {
        List<String> candidates = new ArrayList<>();
        for (int i = 0, cur = 0, last = 0, n = s.length(); i < n; i++) {
            cur += s.charAt(i) == '1' ? 1 : -1;
            if (cur == 0) {
                candidates.add(String.format("1%s0", makeLargestSpecial(s.substring(last + 1, i))));
                last = i + 1;
            }
        }
        StringBuilder sb = new StringBuilder();
        Collections.sort(candidates, (a, b) -> b.compareTo(a));
        for (String str: candidates) {
            sb.append(str);
        }
        return sb.toString();
    }
}
```
```TypeScript []
function makeLargestSpecial(s: string): string {
    const candidates = new Array<string>()
    for (let i = 0, cur = 0, last = 0; i < s.length; i++) {
        cur += s.charCodeAt(i) === '1'.charCodeAt(0) ? 1 : -1
        if (cur == 0) {
            candidates.push("1" + makeLargestSpecial(s.substring(last + 1, i)) + "0")
            last = i + 1
        }
    }
    candidates.sort((a, b) => b.localeCompare(a))
    return candidates.join("")
};
```
```Go []
func makeLargestSpecial(s string) string {
    candidates := sort.StringSlice{}
    for i, cur, last := 0, 0, 0; i < len(s); i++ {
        if s[i] == '1' {
            cur++
        } else {
            cur--
        }
        if cur == 0 {
            candidates = append(candidates, "1" + makeLargestSpecial(s[last+1:i]) + "0")
            last = i + 1
        }
    }
    sort.Sort(sort.Reverse(candidates))
    return strings.Join(candidates, "")
}
```
