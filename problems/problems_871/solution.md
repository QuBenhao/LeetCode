# [Python/Java/TypeScript/Go] 最大堆

> Author: Benhao
> Date: 2022-07-02
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
每次都走当前的油的距离，将经过的加油站的油都加入最大堆中。
如果走到的距离没超过目标距离，从累计到的油中选油最多的那次加油（收益最大）。
重复以上步骤。

### 代码

```Python3 []
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuels = []
        cur, idx, fuel, ans = 0, 0, startFuel, 0
        while cur < target:
            cur += fuel
            while idx < len(stations) and stations[idx][0] <= cur:
                heapq.heappush(fuels, -stations[idx][1])
                idx += 1
            if cur < target:
                if not fuels:
                    break
                else:
                    fuel = -heapq.heappop(fuels)
                    ans += 1
        return ans if cur >= target else -1
```
```Java []
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
        int cur = 0, ans = 0;
        for (int idx = 0, fuel = startFuel; cur < target; ) {
            cur += fuel;
            while (idx < stations.length && stations[idx][0] <= cur) {
                pq.add(stations[idx++][1]);
            }
            if (cur < target) {
                if (pq.isEmpty()) {
                    break;
                }
                ans++;
                fuel = pq.poll();
            }
        }
        return cur >= target ? ans : -1;
    }
}
```
```TypeScript []
function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    const pq = new PriorityQueue<number>((a, b) => a > b)
    let ans = 0
    for (let cur = 0, idx = 0, fuel = startFuel; cur < target; ) {
        cur += fuel
        while (idx < stations.length && stations[idx][0] <= cur) {
            pq.offer(stations[idx++][1])
        }
        if (cur < target) {
            if (pq.data.length == 0) {
                return -1
            }
            fuel = pq.poll()
            ans++
        }
    }
    return ans
};

class PriorityQueue<T> {
    data: Array<T>
    size: number
    compare: Function
  constructor(
    compare = (a: T, b: T) => a[0] > b[0] 
    ){
    this.data = []
    this.size = 0
    this.compare = compare
  }

  isEmpty(): boolean {
      return this.size === 0
  }

  peek(): T {
    return this.size === 0 ? null : this.data[0] 
  }

  offer(val: T): void {
    this.data.push(val)
    this._shifUp(this.size++)
  }

  poll(): T {
    if(this.size === 0) { return null }
    this._swap(0, --this.size)
    this._shifDown(0)
    return this.data.pop()
  }

  _parent(index: number): number {
    return index - 1 >> 1
  }
  
  _child(index: number): number {
    return (index << 1) + 1
  }

  _shifDown(index: number): void {
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

  _shifUp(index: number): void {
    while(this._parent(index) >= 0 
    && this.compare(this.data[index], this.data[this._parent(index)])) {
      this._swap(index, this._parent(index))
      index = this._parent(index)
    }
  }

  _swap(a: number, b: number): void {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]]
  }
}
```
```Go []
func minRefuelStops(target int, startFuel int, stations [][]int) (ans int) {
    pq := &IntHeap{}
    for cur, idx, fuel := 0, 0, startFuel; cur < target; {
        cur += fuel
        for idx < len(stations) && stations[idx][0] <= cur {
            heap.Push(pq, stations[idx][1])
            idx++
        }
        if cur < target {
            if pq.Len() == 0 {
                return -1
            }
            ans++
            fuel = heap.Pop(pq).(int)
        }
    }
    return
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