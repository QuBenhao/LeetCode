# [Python/Java/TypeScript/Go] 队列模拟

> slug: pythonjavatypescriptgo-by-himymben-4fo1
> date: 2022-07-15
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: 数据流中的移动平均值 (qIsx9U)
> url: https://leetcode.cn/problems/qIsx9U/solutions/4eZAFW/pythonjavatypescriptgo-by-himymben-4fo1/

---
### 解题思路
队列模拟滑动窗口即可。
注意使用一个变量维护滑动窗口的总和，避免反复重复计算滑窗内的和。

### 代码

```Python3 []
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue, self.size, self.sum = deque(), size, 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```
```Java []
class MovingAverage {
    private final Deque<Integer> queue;
    private int sum, size;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        queue = new ArrayDeque<>(size);
        sum = 0;
        this.size = size;
    }
    
    public double next(int val) {
        if (queue.size() == size) {
            sum -= queue.removeFirst();
        }
        queue.addLast(val);
        sum += val;
        return (0.0 + sum) / queue.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
```
```TypeScript []
class MovingAverage {

    queue: Array<number>
    size: number
    sum: number
    idx: number

    constructor(size: number) {
        this.queue = new Array<number>()
        this.size = size
        this.sum = 0
        /**
         *  找不到自己队列的模板了突然，只能指针了先
         */
        this.idx = 0
    }

    next(val: number): number {
        if (this.queue.length - this.idx == this.size) {
            this.sum -= this.queue[this.idx++]
        }
        this.queue.push(val)
        this.sum += val
        return this.sum / (this.queue.length - this.idx)
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
```
```TypeScript []
class MovingAverage {

    queue: MyQueue<number>
    size: number
    sum: number

    constructor(size: number) {
        this.queue = new MyQueue<number>()
        this.size = size
        this.sum = 0
    }

    next(val: number): number {
        if (this.queue.length == this.size) {
            this.sum -= this.queue.dequeue()
        }
        this.queue.enqueue(val)
        this.sum += val
        return this.sum / this.queue.length
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

// https://github.com/yangshun/lago

export interface AbstractNode {
  next?: AbstractNode | null;
  prev?: AbstractNode | null;
}

class Node<T> implements AbstractNode {
  public value: T;

  public next: AbstractNode | null;

  public prev: AbstractNode | null;

  constructor(value: T) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DummyHeadNode implements AbstractNode {
  public next: AbstractNode | null;

  constructor() {
    this.next = null;
  }
}

class DummyTailNode implements AbstractNode {
  public prev: AbstractNode | null;

  constructor() {
    this.prev = null;
  }
}

class MyQueue<T> {
  private _dummyHead: DummyHeadNode;

  private _dummyTail: DummyTailNode;

  private _length: number;

  constructor() {
    this._dummyHead = new DummyHeadNode();
    this._dummyTail = new DummyTailNode();
    this._dummyHead.next = this._dummyTail;
    this._dummyTail.prev = this._dummyHead;
    this._length = 0;
  }

  /**
   * Adds an element to the back of the Queue.
   * @param {*} element
   * @return {number} The new length of the Queue.
   */
  enqueue(value: T): number {
    const node = new Node(value);
    const prevLast = this._dummyTail.prev as Node<T> | DummyHeadNode;
    prevLast.next = node;

    node.prev = prevLast;
    node.next = this._dummyTail;
    this._dummyTail.prev = node;
    this._length++;
    return this._length;
  }

  /**
   * Removes the element at the front of the Queue.
   * @return {*} The element at the front of the Queue.
   */
  dequeue(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    const node = this._dummyHead.next as Node<T>;
    const newFirst = node.next as Node<T> | DummyTailNode;
    this._dummyHead.next = newFirst;
    newFirst.prev = this._dummyHead;
    node.next = null;
    this._length--;
    return node.value;
  }

  /**
   * Returns true if the Queue has no elements.
   * @return {boolean} Whether the Queue has no elements.
   */
  isEmpty(): boolean {
    return this._length === 0;
  }

  /**
   * Returns the element at the front of the Queue.
   * @return {*} The element at the front of the Queue.
   */
  front(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return (this._dummyHead.next as Node<T>).value;
  }

  /**
   * Returns the element at the back of the Queue.
   * @return {*} The element at the back of the Queue.
   */
  back(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return (this._dummyTail.prev as Node<T>).value;
  }

  /**
   * Returns the number of elements in the Queue.
   * @return {number} Number of elements in the Queue.
   */
  get length(): number {
    return this._length;
  }
}
```
```Go []
type MovingAverage struct {
    Queue []int
    Size int
    Sum int
}


/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {
    return MovingAverage{[]int{}, size, 0}
}


func (this *MovingAverage) Next(val int) float64 {
    if len(this.Queue) == this.Size {
        this.Sum -= this.Queue[0]
        this.Queue = this.Queue[1:]
    }
    this.Queue = append(this.Queue, val)
    this.Sum += val
    return float64(this.Sum) / float64(len(this.Queue))
}


/**
 * Your MovingAverage object will be instantiated and called as such:
 * obj := Constructor(size);
 * param_1 := obj.Next(val);
 */
```