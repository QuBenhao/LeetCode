# [Python] 贪心

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 16
> Tags: Python, Python3

---

### 解题思路
不要急着选自己最高的，要综合对方的来看(我们要拿走综合最高的，这样我们拿到的减去对方拿到的才能尽可能大)

假设两个石子，价值分别是$a_1, a_2$ 和 $b_1, b_2$，
其结果分别为$a_1 - b_2$和$a_2 - b_1$.
做差比较两者的大小得到$a_1 - b_2 - a_2 + b_1 = (a_1 + b_1) - (a_2 + b_2)$.

在博弈中，我们拿到的石子，相当于我们拿到了这个石子并且杜绝了对方拿到这个石子，由于对方对于我们来说是减法，所以杜绝对方拿到相当于做了加法。


### 代码

```python3
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        totalValues = [(a+b) for a,b in zip(aliceValues, bobValues)]
        totalValues.sort(reverse=True)
        # 所有Alice能拿到的石头的总价值，其中每个都多拿了Bob的对应石子,再减去本来就是Bob拿的石子，正好是Bob的所有石子
        ans = sum(totalValues[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
```