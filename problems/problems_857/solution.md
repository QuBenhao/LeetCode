# [Python/Java/TypeScript/Go] 性价比 + 工作质量大顶堆

> Author: Benhao
> Date: 2022-09-11
> Upvotes: 29
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
每个工人的性价比是期望工资除以质量，k组员工的性价比由性价比最高的人决定，最终总开支由性价比和总工作质量决定。
我们希望性价比尽可能低，且总工作质量尽可能低。
从小到大遍历性价比，这样当前组合的性价比就是当前性价比。我们维护一个取工作质量最小的方式即可。

### 代码

```Python3 []
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans, total, pq = inf, 0, []
        for q, w in sorted(zip(quality, wage), key=lambda x: (x[1] / x[0])):
            total += q
            heapq.heappush(pq, -q)
            if len(pq) > k:
                total += heapq.heappop(pq)
            if len(pq) == k:
                ans = min(ans, total *  w / q)
        return ans
```
```Java []
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        double ans = -1;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
        int total = 0;
        Integer[] ids = new Integer[quality.length];
        for (int i = 0; i < quality.length; i++) {
            ids[i] = i;
        }
        Arrays.sort(ids, (i, j) -> quality[j] * wage[i] - quality[i] * wage[j]);
        for (int idx: ids) {
            total += quality[idx];
            pq.add(quality[idx]);
            if (pq.size() > k) {
                total -= pq.poll();
            }
            if (pq.size() == k) {
                double cur = (double)total * wage[idx] / quality[idx];
                ans = ans < 0 ? cur : Math.min(ans, cur);
            }
        }
        return ans;
    }
}
```
```TypeScript []
function mincostToHireWorkers(quality: number[], wage: number[], k: number): number {
    let ans: number = -1, total: number = 0
    const pq = new MaxPriorityQueue(), ids: Array<number> = new Array<number>(quality.length).fill(0).map((_, index) => index)
    ids.sort((i, j) => wage[i] * quality[j] - wage[j] * quality[i])
    for (const idx of ids) {
        total += quality[idx]
        pq.enqueue(quality[idx])
        if (pq.size() > k) {
            total -= pq.dequeue().element
        }
        if (pq.size() == k) {
            const cur: number = wage[idx] * total / quality[idx]
            ans = ans < 0 ? cur : Math.min(ans, cur)
        }
    }
    return ans
};
```
```Go []
func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
    ans, total, pq, ids := -1.0, 0, &IntHeap{}, make([]int, len(quality))
    for i := 0; i < len(quality); i++ {
        ids[i] = i
    }
	sort.Slice(ids, func(i, j int) bool {return wage[ids[i]] * quality[ids[j]] < wage[ids[j]] * quality[ids[i]]})
    for _, idx := range ids {
        total += quality[idx]
        heap.Push(pq, quality[idx])
        if pq.Len() > k {
            total -= heap.Pop(pq).(int)
        }
        if pq.Len() == k {
            if cur := float64(total) * float64(wage[idx]) / float64(quality[idx]); ans == -1 || ans > cur {
                ans = cur
            }
        }
    }
    return ans
}


type IntHeap []int
func (h IntHeap) Len() int{return len(h)}
func (h IntHeap) Less(i, j int) bool{return h[i] > h[j]}
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i]}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]
    return x
}
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
```