# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-09-06
> Upvotes: 22
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
统计空格数和单词数，按题意拼接

### 代码

```Python3 []
class Solution:
    def reorderSpaces(self, text: str) -> str:
        return (" " * (space // (len(sp) - 1))).join(sp) + " " * (space % (len(sp) - 1)) if (space := text.count(" ")) and len(sp := text.split()) > 1 else (sp[0] + " " * space if space else text)
```
```Java []
class Solution {
    public String reorderSpaces(String text) {
        List<String> list = new ArrayList<>();
        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                if (sb.length() > 0) {
                    list.add(sb.toString());
                    sb.setLength(0);
                }
                count++;
            } else {
                sb.append(text.charAt(i));
            }
        }
        if (sb.length() > 0) {
            list.add(sb.toString());
            sb.setLength(0);
        }
        int len = list.size() - 1;
        for (int i = 0; i < len; i++) {
            sb.append(list.get(i));
            sb.append(" ".repeat(count / len));
        }
        sb.append(list.get(len));
        sb.append(" ".repeat(len == 0 ? count : count % len));
        return sb.toString();
    }
}
```
```TypeScript []
function reorderSpaces(text: string): string {
    const words: string[] = text.trim().split(/\s+/), count: number = text.match(/ /g)?.length || 0;
    let ans: string;
    if (words.length > 1) {
        ans = words.join(" ".repeat(Math.floor(count / (words.length - 1))))
    } else {
        ans = words[0]
    }
    return ans + " ".repeat(words.length > 1 ? count % (words.length - 1) : count)
};
```
```Go []
func reorderSpaces(text string) string {
    sp, count := strings.Fields(text), strings.Count(text, " ")
    if size := len(sp) - 1; size == 0 {
        return sp[0] + strings.Repeat(" ", count)
    } else {
        return strings.Join(sp, strings.Repeat(" ", count / size)) + strings.Repeat(" ", count % size)
    }
}
```