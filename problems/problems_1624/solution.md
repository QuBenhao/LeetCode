# [Python/Java/TypeScript/Go] 模拟 

> slug: pythonjavatypescriptgo-by-himymben-k4kr
> date: 2022-09-17
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Largest Substring Between Two Equal Characters (largest-substring-between-two-equal-characters)
> url: https://leetcode.cn/problems/largest-substring-between-two-equal-characters/solutions/a8yWAT/pythonjavatypescriptgo-by-himymben-k4kr/

---
### 解题思路
根据题意统计每个字母最左最右坐标，最终求最大值即可

### 代码

```python3
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = defaultdict(list)
        for i, c in enumerate(s):
            mp[c].append(i)
        return max(v[-1] - v[0] - 1 for v in mp.values())
```
```Python3 []
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(s.rfind(c) - s.find(c) - 1 for c in string.ascii_lowercase)
```
```Java []
class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int ans = -1;
        for (int i = 0; i < 26; i++) {
            ans = Math.max(ans, s.lastIndexOf(97 + i) - s.indexOf(97 + i) - 1);
        }
        return ans;
    }
}
```
```TypeScript []
function maxLengthBetweenEqualCharacters(s: string): number {
    let ans: number = -1
    for (let i = 0; i < 26; i++) {
        const sub: string = String.fromCharCode(97 + i)
        ans = Math.max(ans, s.lastIndexOf(sub) - s.indexOf(sub) - 1)
    }
    return ans
};
```
```Go []
func maxLengthBetweenEqualCharacters(s string) int {
    ans := -1
    for i := 0; i < 26; i++ {
        sub := string(rune(97 + i))
        if cur := strings.LastIndex(s, sub) - strings.Index(s, sub) - 1; cur > ans {
            ans = cur
        }
    }
    return ans
}
```