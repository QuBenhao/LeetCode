# [Python/Java/JavaScript/Go] 多路归并应用题

> Author: Benhao
> Date: 2022-01-13
> Upvotes: 38
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
和[786. 第 K 个最小的素数分数](https://leetcode.cn/problems/k-th-smallest-prime-fraction/solution/pythonjavajavascriptgo-zui-xiao-dui-by-h-l2z3/)在做法上无任何区别。

### 代码

```Python3 []
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq, ans = [(num + nums2[0], i, 0) for i, num in enumerate(nums1[:k])], []
        heapq.heapify(pq)
        while pq and k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return ans
```
```Java []
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((x, y) -> nums1[x[0]] + nums2[x[1]] - nums1[y[0]] - nums2[y[1]]);
        for(int i=0;i<Math.min(k, nums1.length);i++){
            pq.offer(new int[]{i, 0});
        }
        List<List<Integer>> ans = new ArrayList<>();
        while(pq.size() > 0 && k-- > 0){
            int[] cur = pq.poll();
            ans.add(new ArrayList<Integer>(){{add(nums1[cur[0]]); add(nums2[cur[1]]);}});
            if(cur[1] < nums2.length - 1)
                pq.offer(new int[]{cur[0], cur[1] + 1});
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function(nums1, nums2, k) {
    const pq = new PriorityQueue(), ans = new Array()
    for(let i=0;i<Math.min(k, nums1.length);i++)
        pq.offer([nums1[i] + nums2[0], i, 0])
    while(pq.size > 0 && k-- > 0){
        const cur = pq.poll()
        ans.push([nums1[cur[1]], nums2[cur[2]]])
        if(cur[2] < nums2.length - 1)
            pq.offer([nums1[cur[1]] + nums2[cur[2] + 1], cur[1], cur[2] + 1])
    }
    return ans
};

class PriorityQueue {
  constructor(
    compare = (a, b) => a[0] - b[0] < 0
    ){
    this.data = []
    this.size = 0
    this.compare = compare
  }

  peek() {
    return this.size === 0 ? null : this.data[0] 
  }

  offer(val) {
    this.data.push(val)
    this._shifUp(this.size++)
  }

  poll() {
    if(this.size === 0) { return null }
    this._swap(0, --this.size)
    this._shifDown(0)
    return this.data.pop()
  }

  _parent(index) {
    return index - 1 >> 1
  }
  
  _child(index) {
    return (index << 1) + 1
  }

  _shifDown(index) {
    while(this._child(index) < this.size) {
      let child = this._child(index)
      if(child + 1 < this.size 
        && this.compare(this.data[child + 1], this.data[child])) {
          child = child + 1
      }
      if(this.compare(this.data[index], this.data[child])){
        break
      }
      this._swap(index, child)
      index = child
    }
  }

  _shifUp(index) {
    while(this._parent(index) >= 0 
    && this.compare(this.data[index], this.data[this._parent(index)])) {
      this._swap(index, this._parent(index))
      index = this._parent(index)
    }
  }

  _swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]]
  }
}
```
```Go []
func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
    n1, n2, ans := len(nums1), len(nums2), [][]int{}
    if n1 > k {
        n1 = k
    }
    pq := make(hp, n1)
    for i := 0; i < n1; i++ {
        pq[i] = []int{nums1[i] + nums2[0], i, 0}
    }
    // 相当于heapq.heapify
    heap.Init(&pq)
    for pq.Len() > 0 && k > 0 {
        k--
        cur := heap.Pop(&pq).([]int)
        ans = append(ans, []int{nums1[cur[1]], nums2[cur[2]]})
        if cur[2] < n2 - 1 {
            heap.Push(&pq, []int{nums1[cur[1]] + nums2[cur[2] + 1], cur[1], cur[2] + 1})
        }
    }
    return ans
}
// 最小堆模板
type hp [][]int
func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i][0] < h[j][0] }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.([]int)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
```