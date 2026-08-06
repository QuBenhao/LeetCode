# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-rayz
> date: 2022-01-23
> tags: Go, Java, JavaScript, Python, Python3
> question: Stock Price Fluctuation  (stock-price-fluctuation)
> url: https://leetcode.cn/problems/stock-price-fluctuation/solutions/5w4ebP/pythonjavajavascriptgo-mo-ni-by-himymben-rayz/

---
### 解题思路
维护一个最大的时间戳，维护一个价格的有序列表（在相同时间戳更新价格时删掉原来错误的时间戳）

### 代码

```Python3 []
from sortedcontainers import SortedList
class StockPrice:
    def __init__(self):
        self.sl = SortedList()
        self.time_map = {}
        self.max_time = -inf

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_map:
            self.sl.discard(self.time_map[timestamp])
        self.sl.add(price)
        self.time_map[timestamp] = price
        self.max_time = max(self.max_time, timestamp)

    def current(self) -> int:
        return self.time_map[self.max_time]

    def maximum(self) -> int:
        return self.sl[-1]

    def minimum(self) -> int:
        return self.sl[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
```
```Java []
class StockPrice {
    private int maxTime;
    private Map<Integer, Integer> timeMap;
    private TreeMap<Integer, Integer> priceMap;
    public StockPrice() {
        maxTime = 0;
        timeMap = new HashMap<>();
        priceMap = new TreeMap<>();
    }
    
    public void update(int timestamp, int price) {
        if(timeMap.containsKey(timestamp)){
            int oldPrice = timeMap.get(timestamp);
            int cnt = priceMap.get(oldPrice);
            if(cnt == 1)
                priceMap.remove(oldPrice);
            else
                priceMap.put(oldPrice, cnt - 1);
        }
        timeMap.put(timestamp, price);
        priceMap.put(price, priceMap.getOrDefault(price, 0) + 1);
        maxTime = Math.max(maxTime, timestamp);
    }
    
    public int current() {
        return timeMap.get(maxTime);
    }
    
    public int maximum() {
        return priceMap.lastKey();
    }
    
    public int minimum() {
        return priceMap.firstKey();
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
```
```JavaScript []
var StockPrice = function() {
    this.maxTime = 0
    this.timeMap = new Map()
    this.maxPrice = new PriorityQueue((a, b)=>a[0] - b[0] > 0)
    this.minPrice = new PriorityQueue((a, b)=>a[0] - b[0] < 0)
};

/** 
 * @param {number} timestamp 
 * @param {number} price
 * @return {void}
 */
StockPrice.prototype.update = function(timestamp, price) {
    this.maxTime = Math.max(timestamp, this.maxTime)
    this.timeMap.set(timestamp, price)
    this.maxPrice.offer([price, timestamp])
    this.minPrice.offer([price, timestamp])
};

/**
 * @return {number}
 */
StockPrice.prototype.current = function() {
    return this.timeMap.get(this.maxTime)
};

/**
 * @return {number}
 */
StockPrice.prototype.maximum = function() {
    while(true){
        const cur = this.maxPrice.peek()
        if(this.timeMap.get(cur[1]) === cur[0])
            return cur[0]
        this.maxPrice.poll()
    }
};

/**
 * @return {number}
 */
StockPrice.prototype.minimum = function() {
    while(true){
        const cur = this.minPrice.peek()
        if(this.timeMap.get(cur[1]) === cur[0])
            return cur[0]
        this.minPrice.poll()
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = new StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */

 class PriorityQueue {
  constructor(
    compare = (a, b) => a < b 
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
type StockPrice struct {
    maxTime int
    timeMap map[int]int
    maxPrice, minPrice IntHeap
}


func Constructor() StockPrice {
    return StockPrice{timeMap:map[int]int{}}
}


func (this *StockPrice) Update(timestamp int, price int)  {
    if this.maxTime < timestamp {
        this.maxTime = timestamp
    }
    this.timeMap[timestamp] = price
    heap.Push(&this.maxPrice, []int{-price, timestamp})
    heap.Push(&this.minPrice, []int{price, timestamp})
}


func (this *StockPrice) Current() int {
    return this.timeMap[this.maxTime]
}


func (this *StockPrice) Maximum() int {
    for {
        cur := heap.Pop(&this.maxPrice).([]int)
        v := this.timeMap[cur[1]]
        if v == -cur[0] {
            heap.Push(&this.maxPrice, cur)
            return v
        }
    }
}


func (this *StockPrice) Minimum() int {
    for {
        cur := heap.Pop(&this.minPrice).([]int)
        v := this.timeMap[cur[1]]
        if v == cur[0] {
            heap.Push(&this.minPrice, cur)
            return v
        }
    }
}


/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */

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