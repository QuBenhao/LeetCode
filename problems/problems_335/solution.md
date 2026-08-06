# [Python] 今天做一个搬运工

> slug: python-fan-yi-guan-by-himymben-c85r
> date: 2021-10-28
> tags: Python, Python3
> question: Self Crossing (self-crossing)
> url: https://leetcode.cn/problems/self-crossing/solutions/6xbf6y/python-fan-yi-guan-by-himymben-c85r/

---
### 解题思路
今天不想纠结这题了，感觉就是把每种相交的情况枚举一下…做一个翻译官了...[三叶姐姐的题解](https://leetcode.cn/problems/self-crossing/solution/gong-shui-san-xie-fen-qing-kuang-tao-lun-zdrb/)

### 代码

```python3
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        l = len(distance)
        if l <= 3:
            return False
        for i in range(3, l):
            # 第四条线与第一条线相交  (所有相隔三个的情况都通用)
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # 第五条线与第一条线相交 （所有相隔四个的情况都通用）
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            # 第六条线与第一条线相交 （所有相隔五个的情况都通用）
            if i >= 5 and distance[i-2] - distance[i-4] >= 0 and distance[i] >= distance[i-2] - distance[i-4] and distance[i-1] >= distance[i-3] - distance[i-5] and distance[i-1] <= distance[i-3]:
                return True
        return False
```