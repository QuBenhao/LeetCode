# [Python/Java/JavaScript/Go] 队列模拟

> slug: pythonjavajavascriptgo-by-himymben-h9p5
> date: 2022-05-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Number of Recent Calls (number-of-recent-calls)
> url: https://leetcode.cn/problems/number-of-recent-calls/solutions/Q3wRs7/pythonjavajavascriptgo-by-himymben-h9p5/

---
### 解题思路
就每次把超时的踢掉

PS:
js使用[队列](https://github.com/datastructures-js/queue)

### 代码

```Python3 []
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```
```Java []
class RecentCounter {
    private Deque<Integer> queue;

    public RecentCounter() {
        queue = new ArrayDeque<>();
    }
    
    public int ping(int t) {
        while(!queue.isEmpty() && queue.peekFirst() < t - 3000)
            queue.pollFirst();
        queue.addLast(t);
        return queue.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
```
```JavaScript []
var RecentCounter = function() {
    this.queue = new Queue()
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    while(this.queue.size() > 0 && this.queue.front() < t - 3000)
        this.queue.dequeue()
    this.queue.enqueue(t)
    return this.queue.size()
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```
```Go []
type RecentCounter struct {
    queue []int
}


func Constructor() RecentCounter {
    return RecentCounter{}
}


func (this *RecentCounter) Ping(t int) int {
    for len(this.queue) > 0 && this.queue[0] < t - 3000 {
        this.queue = this.queue[1:]
    }
    this.queue = append(this.queue, t)
    return len(this.queue)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
```