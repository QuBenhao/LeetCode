# [Python/Java] Greedy max-heap

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 2
> Tags: Java, Python, Python3

---

### Approach
Reducing the largest number each time gives the largest benefit.

In Python, floor division of a negative value corresponds to ceiling division of its positive counterpart. In Java, configure a priority queue as a max-heap.

### Code

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
