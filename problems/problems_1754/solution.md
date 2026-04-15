# [Python] 贪心

> Author: Benhao
> Date: 2022-12-24
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

始终从字典序更大的那个字符串取首字母

```Python3 []
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        q1, q2, ans = deque(word1), deque(word2), []
        while q1 or q2:
            if q1 > q2:
                ans.append(q1.popleft())
            else:
                ans.append(q2.popleft())
        ans.append(word1[len(word1) - len(q1):])
        ans.append(word2[len(word2) - len(q2):])
        return "".join(ans)
```
```Go []
func largestMerge(word1 string, word2 string) string {
    var sb strings.Builder
    for len(word1) > 0 && len(word2) > 0 {
        if word1 > word2 {
            sb.WriteByte(word1[0])
            word1 = word1[1:]
        } else {
            sb.WriteByte(word2[0])
            word2 = word2[1:]
        }
    }
    sb.WriteString(word1)
    sb.WriteString(word2)
    return sb.String()
}
```