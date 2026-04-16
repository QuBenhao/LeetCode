# [Python/Java/TypeScript/Go] 递归

> Author: Benhao
> Date: 2022-08-07
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
参考了[大佬的题解](https://leetcode.cn/problems/special-binary-string/solution/zhuan-huan-wei-gua-hao-zi-fu-chuan-jiu-hen-rong-yi/)，
将1看成左括号，0看成右括号，实际上是一道有效的括号问题。
最终要让前面左括号尽可能多。

### 代码

```Python3 []
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # cur: 前缀和统计, last: 上一个特殊序列的结尾
        cur = last = 0
        # 所有可选的子特殊序列
        candidates = []
        for i, c in enumerate(s):
            cur += 1 if c == '1' else -1
            # 出现特殊序列, 一定是以1开头以0结尾
            if not cur:
                # 先将当前特殊序列排成最大, 首尾最终仍是1和0不可动，所以递归去掉头尾
                candidates.append('1' + self.makeLargestSpecial(s[last + 1:i]) + '0')
                last = i + 1
        # 所有特殊子序列可以无限次交换，因此从大到小依次排列拼接即可
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