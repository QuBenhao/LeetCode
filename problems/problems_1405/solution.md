# [Python/Java/JavaScript/Go] 贪心

> slug: pythonjavajavascriptgo-tan-xin-by-himymb-iep8
> date: 2022-02-07
> tags: Go, Java, JavaScript, Python, Python3
> question: Longest Happy String (longest-happy-string)
> url: https://leetcode.cn/problems/longest-happy-string/solutions/yr0F1G/pythonjavajavascriptgo-tan-xin-by-himymb-iep8/

---
### 解题思路
递归写法：
每次添加一个当前最多的字符到答案中，最多连续两个相同的字符，如果还要添加该字符，必须从剩下字符里先添加一个其他最多的字符。

### 代码

```Python3 []
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def addChars(queue, strs):
            val, char = heapq.heappop(queue)
            if not val or (len(strs) >= 2 and strs[-2] == strs[-1] == char and (not queue or not addChars(queue, strs))):
                return False
            strs.append(char)
            heapq.heappush(queue, (val + 1, char))
            return True

        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        ans = []
        while pq and addChars(pq, ans):
            pass
        return "".join(ans)
```
```Java []
class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((x,y)->y[0]-x[0]);
        pq.add(new int[]{a, 0});
        pq.add(new int[]{b, 1});
        pq.add(new int[]{c, 2});
        StringBuilder sb = new StringBuilder();
        while(!pq.isEmpty() && addChar(pq, sb)){}
        return sb.toString();
    }

    private boolean addChar(PriorityQueue<int[]> pq, StringBuilder ans) {
        int[] cur = pq.poll();
        char c = (char)((int)'a' + cur[1]);
        int len = ans.length();
        if(cur[0] == 0 || (len >= 2 && ans.charAt(len - 2) == ans.charAt(len - 1) && ans.charAt(len - 1) == c && (pq.isEmpty() || !addChar(pq, ans))))
            return false;
        ans.append(c);
        cur[0]--;
        pq.add(cur);
        return true;
    }
}
```
```JavaScript []
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
var longestDiverseString = function(a, b, c) {
    const pq = new PriorityQueue((a, b) => a[0] - b[0] > 0), ans = new Array()
    pq.offer([a, 'a'])
    pq.offer([b, 'b'])
    pq.offer([c, 'c'])
    addChar = function(queue, strs) {
        const cur = queue.poll(), len = strs.length
        if(cur[0] == 0 || (len >= 2 && cur[1] == strs[len - 1] && cur[1] == strs[len - 2] && (queue.size == 0 || !addChar(queue, strs))))
            return false
        strs.push(cur[1])
        cur[0]--
        queue.offer(cur)
        return true
    }

    while(pq.size > 0 && addChar(pq, ans)) {}
    return ans.join("")
};

class PriorityQueue {
  constructor(
    compare = (a, b) => a[0] > b[0] 
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
type CharNum struct {
    val int
    char byte
}

func longestDiverseString(a int, b int, c int) string {
    pq, ans := &IntHeap{}, []byte{}
    heap.Push(pq, CharNum{a, 'a'})
    heap.Push(pq, CharNum{b, 'b'})
    heap.Push(pq, CharNum{c, 'c'})
    for pq.Len() > 0 {
        v := addChar(pq, ans)
        if len(ans) == len(v) {
            break
        }
        ans = v
    }
    return string(ans)
}

func addChar(pq *IntHeap, ans []byte) []byte {
    cur := heap.Pop(pq).(CharNum)
    if cur.val == 0 {
        return ans
    } 
    if len(ans) >= 2 && cur.char == ans[len(ans) - 1] && cur.char == ans[len(ans) - 2] {
        if pq.Len() == 0 {
            return ans
        }
        v := addChar(pq, ans)
        if len(ans) == len(v) {
            return ans
        }
        ans = v
    }
    ans = append(ans, cur.char)
    cur.val--
    heap.Push(pq, cur)
    return ans
}

type IntHeap []CharNum
func (h IntHeap) Len() int{return len(h)}
func (h IntHeap) Less(i, j int) bool{return h[i].val > h[j].val}
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i]}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]
    return x
}
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(CharNum))
}
```