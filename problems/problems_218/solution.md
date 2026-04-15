# [Python] 依次遍历所有发生建筑的进出点，记录每个变化点的最高值

> Author: Benhao
> Date: 2021-07-13
> Upvotes: 25
> Tags: Python, Python3

---

### 解题思路
天际线只在建筑的左右点发生，用最小堆记录每个建筑变化的地方(按x坐标排序): 高度为负数是加入了建筑，为正数是删除建筑。(也可以不用堆，直接加入最后排序)

如果加入了的新建筑是最高的，那么天际线发生了变化；
同理，如果删除了一个建筑以后，最高的高度变小了，天际线发生了变化。
为了统计每个点当时所有建筑里最高的高度，我使用了SortedDict充当Counter。实际上也可以直接使用SortedList,就不需要统计高度的个数了，每次判断最高高度是否发生了变化即可。

### 代码
使用SortedDict维护高度
```python3
from sortedcontainers import SortedDict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        changes = []
        for left, right, height in buildings:
            # 加入建筑的左边点
            heapq.heappush(changes, (left, -height))
            # 删除建筑的右边点
            heapq.heappush(changes, (right, height))
        lives = SortedDict()
        # 高度为地平线的建筑始终至少有1个(可以理解为从0到inf有个高度为0的建筑)
        lives[0] = 1
        while changes:
            # 当前的点以及高度
            x, h = heapq.heappop(changes)
            # 加入建筑
            if h < 0:
                if h in lives:
                    lives[h] += 1
                else:
                    lives[h] = 1
                    # 最高建筑
                    if h == lives.keys()[0]:
                        ans.append([x, -h])
            # 删除建筑
            else:
                lives[-h] -= 1
                # 高度为-h的建筑全部没了
                if not lives[-h]:
                    lives.pop(-h)
                    # 判断最高建筑是否发生变化了
                    new_max = lives.keys()[0]
                    if -new_max < h:
                        ans.append([x, -new_max])
        return ans
```
使用SortedList维护高度
```python3
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        changes = []
        for left, right, height in buildings:
            changes.append((left, -height))
            changes.append((right, height))
        # 按变化点的先后排序
        changes.sort()
        # 同样默认有个高度为0
        lives = SortedList([0])
        # 上一个建筑最高高度
        prev = 0
        for x, h in changes:
            # 根据h大小加入或删除建筑
            if h < 0:
                lives.add(h)
            else:
                lives.remove(-h)
            # 加入或删除后当前的最高高度
            curr_max = -lives[0]
            # 最高高度发生了变化
            if curr_max != prev:
                ans.append([x, curr_max])
            prev = curr_max
        return ans
```