# [Python/Java] 最大堆贪心

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 2
> Tags: Java, Python, Python3

---

### 解题思路
每次都降最大的那个数，收益最高

Python里负数向下除相当于正数向上除, Java里用优先队列自制大顶堆。

### 代码

```Python3 []
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        for p in piles:
            heapq.heappush(pq, -p)
        for i in range(k):
            heapq.heappush(pq, heapq.heappop(pq) // 2)
        return -sum(pq)
```
```Java []
class Solution {
    PriorityQueue<Integer> maxHeap;
    public int minStoneSum(int[] piles, int k) {
        maxHeap = new PriorityQueue<Integer>(piles.length,new Comparator<Integer>(){
            @Override
            public int compare(Integer i1,Integer i2){
                return i2-i1;
            }
        });
        int ans = 0;
        for(int p:piles){
            maxHeap.add(p);
            ans += p;
        }
        while(k-- > 0){
            int x = maxHeap.poll();
            ans -= x/2;
            x = (x+1)/2;
            maxHeap.add(x);
        }
        return ans;
    }
}
```