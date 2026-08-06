# [Python/Java/JavaScript/Go] 贪心

> slug: pythonjavajavascriptgo-tan-xin-by-himymb-04rr
> date: 2021-12-13
> tags: Go, Java, JavaScript, Python, Python3
> question: Course Schedule III (course-schedule-iii)
> url: https://leetcode.cn/problems/course-schedule-iii/solutions/2e3wI5/pythonjavajavascriptgo-tan-xin-by-himymb-04rr/

---
### 解题思路
按结束时间排序，可以保证我们优先考虑加入先结束的课程。
在课程塞满的时候，用当前的(如果耗时更短)替换耗时最长的那一个(所以使用优先队列维护时长)，
这样做的意义在于我们用更少的时间完成了相同数量的课程，可以保证后面加入更多课程且不可能比原来的方案的课程少。

### 代码

```Python3 []
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq, t = [], 0
        for duration, lastDay in sorted(courses, key=lambda x:x[1]):
            if t + duration > lastDay and pq and -pq[0] > duration:
                t += heapq.heappop(pq)
            if t + duration <= lastDay:
                heapq.heappush(pq, -duration)
                t += duration
        return len(pq)
```
```Java []
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a,b) -> (a[1] - b[1]));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->(b-a));
        int t = 0;
        for(int[] course: courses){
            if(t + course[0] > course[1] && pq.size() > 0 && pq.peek() > course[0])
                t -= pq.poll();
            if(t + course[0] <= course[1]){
                t += course[0];
                pq.offer(course[0]);
            }
        }
        return pq.size();
    }
}
```
```JavaScript []
/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function(courses) {
    courses.sort((a,b)=>(a[1]-b[1]))
    const pq = new PriorityQueue()
    let t = 0
    for(const course of courses){
        if(t + course[0] > course[1] && pq.size > 0 && pq.peek() > course[0])
            t -= pq.poll()
        if(t + course[0] <= course[1]){
            t += course[0]
            pq.offer(course[0])
        }
    }
    return pq.size
};

class PriorityQueue {
  constructor(
    compare = (a, b) => a > b 
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
func scheduleCourse(courses [][]int) int {
    sort.Slice(courses, func (i, j int) bool {
        return courses[i][1] < courses[j][1]
    })
    pq, t := &Heap{}, 0
    for _, course := range courses {
        d,l := course[0], course[1]
        if t + d > l && pq.Len() > 0 && pq.IntSlice[0] > d {
            t -= heap.Pop(pq).(int)
        }
        if t + d <= l {
            t += d
            heap.Push(pq, d)
        }
    }
    return pq.Len()
}

type Heap struct {
    sort.IntSlice
}

func (h Heap) Less(i, j int) bool {
    return h.IntSlice[i] > h.IntSlice[j]
}

func (h *Heap) Swap(i, j int) {
	h.IntSlice[i], h.IntSlice[j] = h.IntSlice[j], h.IntSlice[i]
}

func (h *Heap) Push(x interface{}) {
    h.IntSlice = append(h.IntSlice, x.(int))
}

func (h *Heap) Pop() interface{} {
    a := h.IntSlice
    x := a[len(a) - 1]
    h.IntSlice = a[:len(a) - 1]
    return x
}
```