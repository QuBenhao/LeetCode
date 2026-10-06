# [Python/Java/TypeScript/Go] A trick

> Author: Benhao
> Date: 2022-08-02
> Upvotes: 30
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
First consider k=1, which allows the fewest operations.
We can only keep moving the first character to the end, so find the smallest string starting at any position.

Next consider k=2. One letter can stay in one of the first two positions while the remaining letters keep rotating.
At any point, this letter can be moved to the end, so a sequence of operations can rearrange the original string into any permutation.
The answer is therefore the sorted string.

### Code

```Python3 []
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else "".join(sorted(s))
```
```Java []
class Solution {
    public String orderlyQueue(String s, int k) {
        if (k == 1) {
            String ans = s;
            StringBuilder sb = new StringBuilder(s);
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                sb.deleteCharAt(0);
                sb.append(c);
                String cur = sb.toString();
                if (cur.compareTo(ans) < 0) {
                    ans = cur;
                }
            }
            return ans;
        } else {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        }
    }
}
```
```TypeScript []
function orderlyQueue(s: string, k: number): string {
    if (k == 1) {
        let ans = s
        for (let i = 0; i < s.length; i++) {
            const cur = s.substring(i, s.length) + s.substring(0, i)
            if (cur < ans) {
                ans = cur
            }
        }
        return ans
    } else {
        return [...s].sort().join("")
    }
};
```
```Go []
func orderlyQueue(s string, k int) string {
    if k == 1 {
        ans := s
        for i := 0; i < len(s); i++ {
            cur := s[i:] + s[:i]
            if cur < ans {
                ans = cur
            }
        }
        return ans
    } else {
        bytes := []byte(s)
        sort.Slice(bytes, func(i, j int) bool {
            return bytes[i] < bytes[j]
        })
        return string(bytes)
    }
}
```
