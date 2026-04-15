# [Python] 找前后相同的位置

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 8
> Tags: Python, Python3

---

### 解题思路
我们找到前后两个'a'，中间的字符就可以构成一个答案。
故记录上一个'a'的index，记录中间的元素数。
单独统计'a'的个数，如果超过2个，答案数+1。

以上'a'为任意字符

### 代码

```python3
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        last_index = [-1] * 26
        count = [0] * 26 
        for i,c in enumerate(s):
            if 0 <= last_index[ord(c)-ord('a')] < i - 1:
                for c_ in set(s[last_index[ord(c)-ord('a')]+1:i]):
                    ans.add(c+c_+c)
            last_index[ord(c)-ord('a')] = i
            count[ord(c)-ord('a')] += 1
        return len(ans) + sum(i >= 3 for i in count)

```