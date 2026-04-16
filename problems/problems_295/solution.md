# [Python/Java] 暴力的有序列表

> Author: Benhao
> Date: 2021-08-26
> Upvotes: 19
> Tags: Java, Python, Python3

---

### 解题思路
维护一个有序列表，属于暴力解法…只适用于竞赛秒题。

常规解法来说，还是应该左边维护一个大顶堆，右边维护一个小顶堆，这样很方便取到中间的值。

### 代码

```Python3
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        return self.nums[n // 2] if (n := len(self.nums)) % 2 else float(self.nums[n//2] + self.nums[(n-1)//2])/2
```
双顶堆
```Python3 []
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.minHeap) - len(self.maxHeap) < -1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return float(self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
```
```Java []
class MedianFinder {
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;
    public MedianFinder() {
        // 左边要大顶堆 （中间的数最大）
        maxHeap = new PriorityQueue<>((a,b) -> b - a);
        // 右边要小顶堆 （中间的数最小）
        minHeap = new PriorityQueue<>((a,b) -> a - b);
    }
    
    public void addNum(int num) {
        // 如果小顶堆没有数，或者插入的数属于小顶堆，先加到小顶堆
        // 否则加到大顶堆
        if(minHeap.size() == 0 || minHeap.peek() <= num)
            minHeap.add(num);
        else
            maxHeap.add(num);
        // 判断两边长度是否差别太大
        if(minHeap.size() - maxHeap.size() > 1)
            maxHeap.add(minHeap.poll());
        else if(maxHeap.size() - minHeap.size() > 1)
            minHeap.add(maxHeap.poll());
    }
    
    public double findMedian() {
        // 总长度为偶数，两边各取一个
        // 否则取更长一点儿的那边的那个
        if(minHeap.size() == maxHeap.size())
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        else if(minHeap.size() > maxHeap.size())
            return minHeap.peek();
        return maxHeap.peek();
    }
}
```