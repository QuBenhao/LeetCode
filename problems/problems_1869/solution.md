# [Python] 按连续的0和1分解字符串

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
匹配连续的0的分解得到所有连续的1的长度的可能性，同理得到0的
比较最大长度即可

### 代码

```python3
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l1 = re.split("0+", s)
        l0 = re.split("1+", s)
        return len(max(l1, key=len)) > len(max(l0, key=len))
```