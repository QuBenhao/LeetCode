# [Python/Java/TypeScript/Go] 模拟 空闲单元法

> Author: Benhao
> Date: 2022-08-01
> Upvotes: 22
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
循环队列中增加一个额外空间，
当队列空的时候，通过`队尾的插入位置 == 队首位置`来判断。
当队列满的时候，通过`(队尾的插入位置 + 1) % 总长度 == 队首位置`来判断。 (`队尾的插入位置 == 队首位置`不再具有二义性)

### 代码

```Python3 []
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.data = [-1] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % len(self.data)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        val = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        return True

    def Front(self) -> int:
        return self.data[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.data[(self.rear - 1) % len(self.data)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.data) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
```Java []
class MyCircularQueue {
    private int[] data;
    private int front, rear;
    public MyCircularQueue(int k) {
        data = new int[k + 1];
        front = rear = 0;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        data[rear] = value;
        rear = getNxt(rear);
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = getNxt(front);
        return true;
    }
    
    public int Front() {
        return isEmpty() ? -1 : data[front];
    }
    
    public int Rear() {
        return isEmpty() ? -1 : data[(rear + data.length - 1) % data.length];
    }
    
    public boolean isEmpty() {
        return front == rear;
    }
    
    public boolean isFull() {
        return getNxt(rear) == front;
    }

    private int getNxt(int cur) {
        return (cur + 1) % data.length;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
```
```TypeScript []
class MyCircularQueue {
    data: number[]
    front: number
    rear: number
    constructor(k: number) {
        this.data = new Array<number>(k + 1).fill(-1)
        this.front = this.rear = 0
    }

    enQueue(value: number): boolean {
        if (this.isFull()) {
            return false
        }
        this.data[this.rear] = value
        this.rear = this.nxt(this.rear)
        return true
    }

    deQueue(): boolean {
        if (this.isEmpty()) {
            return false
        }
        this.front = this.nxt(this.front)
        return true
    }

    Front(): number {
        return this.isEmpty() ? -1 : this.data[this.front]
    }

    Rear(): number {
        return this.isEmpty() ? -1 : this.data[(this.rear + this.data.length - 1) % this.data.length]
    }

    isEmpty(): boolean {
        return this.rear == this.front
    }

    isFull(): boolean {
        return this.nxt(this.rear) == this.front
    }

    nxt(cur: number): number {
        return (cur + 1) % this.data.length
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
```
```Go []
type MyCircularQueue struct {
    Data []int
    Ft int
    Rr int
}


func Constructor(k int) MyCircularQueue {
    return MyCircularQueue{make([]int, k + 1), 0, 0}
}


func (this *MyCircularQueue) EnQueue(value int) bool {
    if (this.IsFull()) {
        return false
    }
    this.Data[this.Rr] = value
    this.Rr = this.Nxt(this.Rr)
    return true
}


func (this *MyCircularQueue) DeQueue() bool {
    if (this.IsEmpty()) {
        return false
    }
    this.Ft = this.Nxt(this.Ft)
    return true
}


func (this *MyCircularQueue) Front() int {
    if (this.IsEmpty()) {
        return -1
    }
    return this.Data[this.Ft]
}


func (this *MyCircularQueue) Rear() int {
    if (this.IsEmpty()) {
        return -1
    }
    return this.Data[(this.Rr - 1 + len(this.Data)) % len(this.Data)]
}


func (this *MyCircularQueue) IsEmpty() bool {
    return this.Rr == this.Ft
}


func (this *MyCircularQueue) IsFull() bool {
    return this.Nxt(this.Rr) == this.Ft
}

func (this *MyCircularQueue) Nxt(cur int) int {
    return (cur + 1) % len(this.Data)
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */
```