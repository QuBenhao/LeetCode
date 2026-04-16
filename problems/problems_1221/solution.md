# [Python/Java] 贪心统计L和R的个数

> Author: Benhao
> Date: 2021-09-07
> Upvotes: 6
> Tags: Java, Python, Python3

---

### 解题思路
因为一开始给出的是平衡字符串，L和R的个数是相等的，也就是说当我们分割出去一个平衡子串后，剩下的L和R的个数依然相等。每次能分出去都分的话，这样分串是最多的。

### 代码

```Python3 []
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = cur = 0
        for c in s:
            if c == 'L':
                cur += 1
            else:
                cur -= 1
            if not cur:
                ans += 1
        return ans
```
```Java []
class Solution {
    public int balancedStringSplit(String s) {
        int ans = 0;
        for(int i=0, cur=0;i<s.length();i++){
            if(s.charAt(i) == 'L')
                cur++;
            else
                cur--;
            if(cur == 0)
                ans++;
        }
        return ans;
    }
}
```