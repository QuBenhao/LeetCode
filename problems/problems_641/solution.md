# [Python/Java/TypeScript/Go] 双向链表

> slug: pythonjavatypescriptgo-shuangxianglianbi-x8p3
> date: 2022-08-14
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Design Circular Deque (design-circular-deque)
> url: https://leetcode.cn/problems/design-circular-deque/solutions/Y1pB5F/pythonjavatypescriptgo-shuangxianglianbi-x8p3/

---
### 解题思路
我们记录双向链表的头，这样在插入头部、插入尾部、断开头部、返回头部、断开尾部、返回尾部都可以做到$O(1)$。

### 代码

```Python3 []
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.head = LinkedNode(-1)
        self.head.next = self.head.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.head.next = LinkedNode(value, self.head, self.head.next)
        self.head.next.next.prev = self.head.next
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.head.prev = LinkedNode(value, self.head.prev, self.head)
        self.head.prev.prev.next = self.head.prev
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if not self.len:
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.len:
            return False
        self.head.prev = self.head.prev.prev
        self.head.prev.next = self.head
        self.len -= 1
        return True

    def getFront(self) -> int:
        return -1 if not self.len else self.head.next.val

    def getRear(self) -> int:
        return -1 if not self.len else self.head.prev.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

class LinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```
```Java []
class MyCircularDeque {
    private final Node head;
    private final int k;
    private int len;
    public MyCircularDeque(int k) {
        head = new Node(-1);
        this.k = k;
        len = 0;
    }
    
    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        head.next = new Node(value, head, head.next);
        head.next.next.prev = head.next;
        len++;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        head.prev = new Node(value, head.prev, head);
        head.prev.prev.next = head.prev;
        len++;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        head.next = head.next.next;
        head.next.prev = head;
        len--;
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        head.prev = head.prev.prev;
        head.prev.next = head;
        len--;
        return true;
    }
    
    public int getFront() {
        return isEmpty() ? -1 : head.next.val;
    }
    
    public int getRear() {
        return isEmpty() ? -1: head.prev.val;
    }
    
    public boolean isEmpty() {
        return len == 0;
    }
    
    public boolean isFull() {
        return len == k;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */

public class Node {
    public final int val;
    public Node prev, next;

    public Node(int val) {
        this.val = val;
        prev = next = this;
    }

    public Node(int val, Node prev, Node next) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}
```
```TypeScript []
class MyCircularDeque {
    k: number
    len: number
    head: LinkedNode
    constructor(k: number) {
        this.k = k
        this.len = 0
        this.head = new LinkedNode(-1, null, null)
        this.head.prev = this.head.next = this.head
    }

    insertFront(value: number): boolean {
        if (this.isFull()) {
            return false
        }
        this.head.next = new LinkedNode(value, this.head, this.head.next)
        this.head.next.next.prev = this.head.next
        this.len++
        return true
    }

    insertLast(value: number): boolean {
        if (this.isFull()) {
            return false
        }
        this.head.prev = new LinkedNode(value, this.head.prev, this.head)
        this.head.prev.prev.next = this.head.prev
        this.len++
        return true
    }

    deleteFront(): boolean {
        if (this.isEmpty()) {
            return false
        }
        this.head.next = this.head.next.next
        this.head.next.prev = this.head
        this.len--
        return true
    }

    deleteLast(): boolean {
        if (this.isEmpty()) {
            return false
        }
        this.head.prev = this.head.prev.prev
        this.head.prev.next = this.head
        this.len--
        return true
    }

    getFront(): number {
        return this.isEmpty() ? this.head.val : this.head.next.val
    }

    getRear(): number {
        return this.isEmpty() ? this.head.val : this.head.prev.val
    }

    isEmpty(): boolean {
        return this.len == 0
    }

    isFull(): boolean {
        return this.len == this.k
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */

class LinkedNode {
    val: number
    prev: LinkedNode
    next: LinkedNode

    constructor(val: number, prev: LinkedNode, next: LinkedNode) {
        this.val = val
        this.prev = prev
        this.next = next
    }
}
```
```Go []
type MyCircularDeque struct {
    Len int
    K int
    Head *Node
}


func Constructor(k int) MyCircularDeque {
    head := ConstructorNode(-1, nil, nil)
    head.Next = &head
    head.Prev = &head
    return MyCircularDeque{0, k, &head}
}


func (this *MyCircularDeque) InsertFront(value int) bool {
    if this.IsFull() {
        return false
    }
    cur := ConstructorNode(value, this.Head, this.Head.Next)
    this.Head.Next = &cur
    this.Head.Next.Next.Prev = this.Head.Next
    this.Len++
    return true
}


func (this *MyCircularDeque) InsertLast(value int) bool {
    if this.IsFull() {
        return false
    }
    cur := ConstructorNode(value, this.Head.Prev, this.Head)
    this.Head.Prev = &cur
    this.Head.Prev.Prev.Next = this.Head.Prev
    this.Len++
    return true
}


func (this *MyCircularDeque) DeleteFront() bool {
    if this.IsEmpty() {
        return false
    }
    this.Head.Next = this.Head.Next.Next
    this.Head.Next.Prev = this.Head
    this.Len--
    return true
}


func (this *MyCircularDeque) DeleteLast() bool {
    if this.IsEmpty() {
        return false
    }
    this.Head.Prev = this.Head.Prev.Prev
    this.Head.Prev.Next = this.Head
    this.Len--
    return true
}


func (this *MyCircularDeque) GetFront() int {
    if this.IsEmpty() {
        return -1
    }
    return this.Head.Next.Val
}


func (this *MyCircularDeque) GetRear() int {
    if this.IsEmpty() {
        return -1
    }
    return this.Head.Prev.Val
}


func (this *MyCircularDeque) IsEmpty() bool {
    return this.Len == 0
}


func (this *MyCircularDeque) IsFull() bool {
    return this.Len == this.K
}


/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */

type Node struct {
    Val int
    Prev *Node
    Next *Node
}

func ConstructorNode(val int, prev *Node, next *Node) Node {
    return Node{val, prev, next}
}
```