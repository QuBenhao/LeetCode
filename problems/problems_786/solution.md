# [Python/Java/JavaScript/Go] 多路归并最小堆 or 二分统计

> slug: pythonjavajavascriptgo-zui-xiao-dui-by-h-l2z3
> date: 2021-11-28
> tags: Go, Java, JavaScript, Python, Python3
> question: K-th Smallest Prime Fraction (k-th-smallest-prime-fraction)
> url: https://leetcode.cn/problems/k-th-smallest-prime-fraction/solutions/vpnZMt/pythonjavajavascriptgo-zui-xiao-dui-by-h-l2z3/

---
### 解题思路
每个素数作为分母时，分子按从小到大的顺序就可以构造该分母下分数的顺序，
我们需要对比的是不同分母之间当前分数的大小，故采用最小堆，将所有当前值加入堆。

今天是复制粘贴Js和Go的最小堆模板的一天

### 代码

```python3 []
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        for i in range(1, len(arr)):
            # 分数、分母坐标、分子坐标
            heapq.heappush(pq, (1/arr[i], i, 0))
        for _ in range(k):
            val, j, i = heapq.heappop(pq)
            if i < j - 1:
                heapq.heappush(pq, (arr[i+1]/arr[j],j,i+1))
        return [arr[i], arr[j]]
```
```Java []
class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        // i1/j1 < i2/j2  ===>  i1 * j2 < i2 * j1
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((x, y) -> arr[x[0]] * arr[y[1]] - arr[y[0]] * arr[x[1]]);
        for(int j=1;j<arr.length;j++){
            pq.offer(new int[]{0, j});
        }
        for(int r=1;r<k;r++){
            int[] cur = pq.poll();
            if(cur[0] < cur[1] - 1)
                pq.offer(new int[]{cur[0]+1, cur[1]});
        }
        return new int[]{arr[pq.peek()[0]], arr[pq.peek()[1]]};
    }
}
```
```JavaScript []
class Heap {
  constructor(compare = (a, b) => a[0] < b[0]) {
    this.heap = []
    this.size = 0
    this.compare = compare
  }

  insert(item) {
    this.heap.push(item)
    this.size += 1
    this.up(this.size - 1)
  }

  remove() {
    const delItem = this.heap[0]
    this.swap(this.size - 1, 0)
    this.size -= 1
    this.heap.length -= 1
    this.down(0)
    return delItem
  }

  down(k) {
    let left = k * 2 + 1,
      right = k * 2 + 2,
      largest = k

    if (left < this.size && this.compare(this.heap[left], this.heap[largest])) {
      largest = left
    }

    if (right < this.size && this.compare(this.heap[right], this.heap[largest])) {
      largest = right
    }

    if (largest !== k) {
      this.swap(k, largest)
      this.down(largest)
    }
  }

  up(k) {
    let parent = Math.floor((k - 1) / 2)
    while (k > 0 && this.compare(this.heap[k], this.heap[parent])) {
      this.swap(k, parent)
      k = parent
      parent = Math.floor((parent - 1) / 2)
    }
  }

  swap(i, j) {
    const tmp = this.heap[i]
    this.heap[i] = this.heap[j]
    this.heap[j] = tmp
  }
}


/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var kthSmallestPrimeFraction = function(arr, k) {
    pq = new Heap();
    for(let j=1;j<arr.length;j++)
        pq.insert([arr[0]/arr[j], 0, j])
    let cur
    for(let r=0;r<k;r++){
        cur = pq.remove()
        if(cur[1] < cur[2] - 1){
            pq.insert([arr[cur[1]+1]/arr[cur[2]], cur[1]+1, cur[2]])
        }
    }
    return [arr[cur[1]],arr[cur[2]]]
};
```
```Go []
func kthSmallestPrimeFraction(arr []int, k int) []int {
    n := len(arr)
    pq := make(hp, n-1)
    for j := 1; j < n; j++ {
        pq[j-1] = frac{arr[0], arr[j], 0, j}
    }
    // 相当于heapq.heapify
    heap.Init(&pq)
    for r := 1; r < k; r++ {
        cur := heap.Pop(&pq).(frac)
        if cur.i+1 < cur.j {
            heap.Push(&pq, frac{arr[cur.i+1], cur.y, cur.i + 1, cur.j})
        }
    }
    return []int{pq[0].x, pq[0].y}
}

type frac struct{ 
    x, y, i, j int 
}

// 最小堆模板
type hp []frac
func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].x*h[j].y < h[i].y*h[j].x }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(frac)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
```

---
二分法
```python3 []
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def find(frac):
            count = ans_m = l = 0
            ans = None
            for j in range(1, len(arr)):
                r = j - 1
                while l < r:
                    mid = (l + r + 1) // 2
                    if arr[mid]/arr[j] <= frac:
                        l = mid
                    else:
                        r = mid - 1
                if arr[l]/arr[j] <= frac:
                    count += l + 1
                    if arr[l]/arr[j] > ans_m:
                        ans_m = arr[l]/arr[j]
                        ans = [arr[l], arr[j]]
            return count, ans
        
        l, r = 0.0, 1.0
        while l - r < 1e-9:
            mid = (l + r) / 2
            cnts, ans = find(mid)
            if cnts == k:
                return ans
            elif cnts > k:
                r = mid
            else:
                l = mid
        return [-1, -1]
```
```Go []
func kthSmallestPrimeFraction(arr []int, k int) []int {
    bs := func(frac float64) []int {
        cnts, ansI, ansJ := 0, 0, len(arr) - 1
        var max float64
        l := 0
        for j := 1; j < len(arr); j++ {
            r := j - 1
            for l < r {
                mid := (l + r + 1) / 2
                if f := float64(arr[mid])/float64(arr[j]); f <= frac {
                    l = mid
                } else {
                    r = mid - 1
                }
            }
            if f := float64(arr[l])/ float64(arr[j]); f <= frac {
                cnts += l + 1
                if f > max {
                    max = f
                    ansI, ansJ = l, j
                }
            }
        }
        return []int{cnts, arr[ansI], arr[ansJ]}
    }

    l, r := 0.0, 1.0
    for l - r < 1e-9 {
        mid := (l + r) / 2
        cur := bs(mid)
        if cur[0] == k {
            return []int{cur[1], cur[2]}
        } else if cur[0] > k {
            r = mid
        } else {
            l = mid
        }
    }
    return []int{-1, -1}
}
```