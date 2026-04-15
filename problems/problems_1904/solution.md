# [Python] 学习官解好好处理在同一个15分钟段的情况

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
这题本质是要数有多少个完整的15分钟区间。自然考虑都转换成分钟算
记得处理在同一个15分钟区间的情况即可 ["12:01", "12:02"]

### 代码

```python3
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        # f到s之间有多少个15分钟, 但是01->29这种不能看做15分钟
        start = int(startTime[:2]) * 60 + int(startTime[3:])
        finish = int(finishTime[:2]) * 60 + int(finishTime[3:])
        # 通宵的情况
        if finish < start:
            # 加一天
            finish += 24 * 60
        # 要正点结束
        finish = finish // 15 * 15
        # 这里开始不再需要调整为正点因为地板除15是一致的
        return (finish - start) // 15 if finish > start else 0

```