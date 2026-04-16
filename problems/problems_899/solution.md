# [Python/Java/TypeScript/Go] 脑筋急转弯

> Author: Benhao
> Date: 2022-08-02
> Upvotes: 30
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
首先考虑了一下k=1的情景，因为这个情况操作最少。
显然我们只能不停地将第一个位置放到最后，那么答案就是从某一个位置开始的，找最小值。

然后考虑了一下k=2的情景，这个时候我发现可以将一个字母放在前两位中的一位，然后剩下的字母可以持续旋转。
在这期间，这个字母可以在任意时刻加入到最后，也就是我们可以通过一定数量的操作将原字符串任意排列，
那答案就是排序啦。

### 代码

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