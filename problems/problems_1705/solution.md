# [Python/Java/JavaScript/Go] 最小堆贪心

> Author: Benhao
> Date: 2021-12-23
> Upvotes: 52
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
核心思路就是每次要吃最先腐烂的苹果，那么要用最小堆按腐烂时间排序，同时记录消耗掉的苹果数（没有苹果了就删除）

**PS**:
兜兜转转刷题一年啦，从只会一点儿Python和Java到现在比较熟练的状态了，再接再厉。也毕业上岸了，希望大家都加油和好运，找到心仪的工作～
好怀念，这是我最早那会儿开始刷题参加周赛时的题目，那时候这题我还错了7、8次到结束也没做出来呢。

![image.png](https://pic.leetcode.cn/1640272572-SjcXbk-image.png)


### 代码

按天数循环写在一起
```Python3 []
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples) or pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if i < len(apples) and apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1]-=1
                ans += 1
                if not pq[0][1]:
                    heapq.heappop(pq)
            i += 1
        return ans
```
```Java []
class Solution {
    public int eatenApples(int[] apples, int[] days) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        int i=0,ans=0,n=apples.length;
        while(i < n || !pq.isEmpty()){
            while(!pq.isEmpty() && pq.peek()[0] <= i)
                pq.poll();
            if(i < n && apples[i] > 0)
                pq.add(new int[]{i+days[i], apples[i]});
            if(!pq.isEmpty()){
                ans++;
                if(--pq.peek()[1] == 0)
                    pq.poll();   
            }
            i++;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} apples
 * @param {number[]} days
 * @return {number}
 */
var eatenApples = function(apples, days) {
    const pq = new PriorityQueue(), n = apples.length
    let i = 0, ans = 0
    while(i < n || pq.size > 0){
        while(pq.size > 0 && pq.peek()[0] <= i)
            pq.poll()
        if(i < n && apples[i] > 0)
            pq.offer([i + days[i], apples[i]])
        if(pq.size > 0){
            ans++
            if(--pq.peek()[1]==0)
                pq.poll()
        }
        i++
    }
    return ans
};


class PriorityQueue {
  constructor(
    compare = (a, b) => a[0] < b[0] 
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
func eatenApples(apples []int, days []int) int {
    pq := &IntHeap{}
    i, ans := 0, 0
    for i < len(apples) || pq.Len() > 0{
        for pq.Len() > 0 && (*pq)[0][0] <= i {
            heap.Pop(pq)
        }
        if i < len(apples) && apples[i] > 0{
            heap.Push(pq, []int{i + days[i], apples[i]})
        }
        if pq.Len() > 0 {
            ans++
            (*pq)[0][1]--
            if (*pq)[0][1] == 0{
                heap.Pop(pq)
            }
        }
        i++
    }
    return ans
}

type IntHeap [][]int
func (h IntHeap) Len() int{return len(h)}
func (h IntHeap) Less(i, j int) bool{return h[i][0] < h[j][0]}
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i]}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]
    return x
}
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.([]int))
}
```

天数结束后直接依次统计 (不需要再一天天遍历剩下的天)
```Python3 []
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1]-=1
                if not pq[0][1]:
                    heapq.heappop(pq)
                ans += 1
            i += 1
        while pq:
            cur = heapq.heappop(pq)
            d = min(cur[0] - i, cur[1])
            i += d
            ans += d
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
        return ans
```
```Java []
class Solution {
    public int eatenApples(int[] apples, int[] days) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        int i=0,ans=0,n=apples.length;
        for(;i<n;i++){
            while(!pq.isEmpty() && pq.peek()[0] <= i)
                pq.poll();
            if(apples[i] > 0)
                pq.add(new int[]{i+days[i], apples[i]});
            if(!pq.isEmpty()){
                ans++;
                if(--pq.peek()[1] == 0)
                    pq.poll();   
            }
        }
        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            int diff = Math.min(cur[0] - i, cur[1]);
            i += diff;
            ans += diff;
            while(!pq.isEmpty() && pq.peek()[0] <= i)
                pq.poll();
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} apples
 * @param {number[]} days
 * @return {number}
 */
var eatenApples = function(apples, days) {
    const pq = new PriorityQueue(), n = apples.length
    let i = 0, ans = 0
    for(;i<n;i++){
        while(pq.size > 0 && pq.peek()[0] <= i)
            pq.poll()
        if(apples[i] > 0)
            pq.offer([i + days[i], apples[i]])
        if(pq.size > 0){
            ans++
            if(--pq.peek()[1]==0)
                pq.poll()
        }
    }
    while(pq.size > 0){
        const cur = pq.poll()
        const d = Math.min(cur[0] - i, cur[1])
        i += d
        ans += d
        while(pq.size > 0 && pq.peek()[0] <= i)
            pq.poll()
    }
    return ans
};


class PriorityQueue {
  constructor(
    compare = (a, b) => a[0] < b[0] 
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
func eatenApples(apples []int, days []int) int {
    pq := &IntHeap{}
    i, ans := 0, 0
    for i < len(apples){
        for pq.Len() > 0 && (*pq)[0][0] <= i {
            heap.Pop(pq)
        }
        if apples[i] > 0{
            heap.Push(pq, []int{i + days[i], apples[i]})
        }
        if pq.Len() > 0 {
            ans++
            (*pq)[0][1]--
            if (*pq)[0][1] == 0{
                heap.Pop(pq)
            }
        }
        i++
    }
    for pq.Len() > 0 {
        cur := heap.Pop(pq).([]int)
        if v := cur[0] - i; v < cur[1] {
            i += v
            ans += v
        }else{
            i += cur[1]
            ans += cur[1]
        }
        for pq.Len() > 0 && (*pq)[0][0] <= i {
            heap.Pop(pq)
        }
    }
    return ans
}

type IntHeap [][]int
func (h IntHeap) Len() int{return len(h)}
func (h IntHeap) Less(i, j int) bool{return h[i][0] < h[j][0]}
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i]}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]
    return x
}
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.([]int))
}
```