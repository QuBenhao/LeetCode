# [Python] 前缀和

> slug: by-himymben-v99n
> date: 2022-04-26
> tags: Python, Python3
> question: Unique Substrings With Equal Digit Frequency (unique-substrings-with-equal-digit-frequency)
> url: https://leetcode.cn/problems/unique-substrings-with-equal-digit-frequency/solutions/zgNc2N/by-himymben-v99n/

---
### 解题思路
习惯性压行然后就发现卡常超时了噗

### 代码

```python3
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        presum = [[0] * 10 for _ in range(len(s) + 1)]
        ans = set()
        for i, c in enumerate(s):
            for j in range(10):
                presum[i + 1][j] = presum[i][j]
            presum[i + 1][o] = presum[i][o := ord(c) - ord('0')] + 1
            for j in range(i + 1):
                m, check = 0, True
                for k in range(10):
                    if diff := presum[i + 1][k] - presum[j][k]:
                        if m and m != diff:
                            check = False
                            break
                        m = diff
                if check:
                    ans.add(s[j:i+1])
        return len(ans)
```