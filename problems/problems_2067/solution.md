# [Python] 前缀和

> slug: python-qian-zhui-he-by-himymben-57lw
> date: 2022-05-02
> tags: Python, Python3
> question: Number of Equal Count Substrings (number-of-equal-count-substrings)
> url: https://leetcode.cn/problems/number-of-equal-count-substrings/solutions/isUWDT/python-qian-zhui-he-by-himymben-57lw/

---
### 解题思路
26 * count 这个范围真绝了，每这个剪枝在count小，字符串长的时候必然超时

### 代码

```python3
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        def check(l, r):
            for i in range(26):
                if (p := presum[r][i] - presum[l][i]) and p != count:
                    return False
            return True

        presum, ans = [[0] * 26 for _ in range(len(s) + 1)], 0
        for i, c in enumerate(s):
            for j in range(26):
                presum[i + 1][j] = presum[i][j]
            presum[i + 1][o] = presum[i][o:=ord(c)-ord('a')] + 1
            for j in range(i - count + 1, max(-1, i - 26 * count), -count):
                ans += int(check(j, i + 1)) 
        return ans

```