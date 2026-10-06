# [Python/Java] Brute force with a sorted list

> Author: Benhao
> Date: 2021-08-26
> Upvotes: 19
> Tags: Java, Python, Python3

---

### Approach
Maintaining a sorted list is a brute-force solution, useful only for solving the problem quickly in a contest.

The standard approach maintains a max-heap on the left and a min-heap on the right, making the middle values easy to retrieve.

### Code

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
Two heaps
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
        // Use a max-heap on the left (the middle value is its maximum)
        maxHeap = new PriorityQueue<>((a,b) -> b - a);
        // Use a min-heap on the right (the middle value is its minimum)
        minHeap = new PriorityQueue<>((a,b) -> a - b);
    }
    
    public void addNum(int num) {
        // Insert into the min-heap if it is empty or the new value belongs there
        // Otherwise, insert into the max-heap
        if(minHeap.size() == 0 || minHeap.peek() <= num)
            minHeap.add(num);
        else
            maxHeap.add(num);
        // Check whether the heap sizes differ too much
        if(minHeap.size() - maxHeap.size() > 1)
            maxHeap.add(minHeap.poll());
        else if(maxHeap.size() - minHeap.size() > 1)
            minHeap.add(maxHeap.poll());
    }
    
    public double findMedian() {
        // For an even total size, take one value from each side
        // Otherwise, take the value from the larger heap
        if(minHeap.size() == maxHeap.size())
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        else if(minHeap.size() > maxHeap.size())
            return minHeap.peek();
        return maxHeap.peek();
    }
}
```
