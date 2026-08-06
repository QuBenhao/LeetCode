# [Python/Java/TypeScript/Go] 双向链表

> slug: pythonjavatypescriptgo-shuang-xiang-lian-khb9
> date: 2022-09-23
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Design Linked List (design-linked-list)
> url: https://leetcode.cn/problems/design-linked-list/solutions/FQzbRL/pythonjavatypescriptgo-shuang-xiang-lian-khb9/

---
### 解题思路
链表模拟

### 代码

```Python3 []
class LinkNode:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt
    
    def add_right(self, node):
        node.nxt = self.nxt
        if node.nxt:
            node.nxt.pre = node
        node.pre = self
        self.nxt = node
    
    def del_right(self):
        self.nxt = self.nxt.nxt
        if self.nxt:
            self.nxt.pre = self

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1, self.head)
        self.head.nxt = self.tail
    
    def getNode(self, index: int) -> LinkNode:
        if index >= self.size or index < 0:
            return None
        if index > self.size // 2:
            node = self.tail
            for _ in range(self.size - index):
                node = node.pre
        else:
            node = self.head
            for _ in range(index + 1):
                node = node.nxt
        return node

    def get(self, index: int) -> int:
        return node.val if (node := self.getNode(index)) else -1

    def addAtHead(self, val: int) -> None:
        self.head.add_right(LinkNode(val))
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.tail.pre.add_right(LinkNode(val))
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            if index <= 0:
                self.addAtHead(val)
            elif index == self.size:
                self.addAtTail(val)
            else:
                self.getNode(index).pre.add_right(LinkNode(val))
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node:
            node.pre.del_right()
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```
```Java []
class LinkNode {
    int val;
    LinkNode pre, nxt;
    
    public LinkNode(int val) {
        this.val = val;
        this.pre = this.nxt = null;
    }

    public LinkNode(int val, LinkNode pre, LinkNode nxt) {
        this.val = val;
        this.pre = pre;
        this.nxt = nxt;
    }

    void addRight(LinkNode node) {
        node.nxt = this.nxt;
        if (node.nxt != null) {
            node.nxt.pre = node;
        }
        this.nxt = node;
        node.pre = this;
    }

    void delRight() {
        this.nxt = this.nxt.nxt;
        if (this.nxt != null) {
            this.nxt.pre = this;
        }
    }
}

class MyLinkedList {
    
    private LinkNode head, tail;
    private int size;

    public MyLinkedList() {
        size = 0;
        head = new LinkNode(-1);
        tail = new LinkNode(-1, head, null);
        head.nxt = tail;
    }

    private LinkNode getNode(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        LinkNode node;
        if (index > size / 2) {
            node = tail;
            for (int i = 0; i < size - index; i++) {
                node = node.pre;
            }
        } else {
            node = head;
            for (int i = 0; i <= index; i++) {
                node = node.nxt;
            }
        }
        return node;
    }
    
    public int get(int index) {
        LinkNode node = getNode(index);
        return node == null ? -1 : node.val;
    }
    
    public void addAtHead(int val) {
        head.addRight(new LinkNode(val));
        size++;
    }
    
    public void addAtTail(int val) {
        tail.pre.addRight(new LinkNode(val));
        size++;
    }
    
    public void addAtIndex(int index, int val) {
        if (index <= size) {
            if (index <= 0) {
                addAtHead(val);
            } else if(index == size) {
                addAtTail(val);
            } else {
                getNode(index).pre.addRight(new LinkNode(val));
                size++;
            }
        }
    }
    
    public void deleteAtIndex(int index) {
        LinkNode node = getNode(index);
        if (node != null) {
            node.pre.delRight();
            size--;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
```
```TypeScript []
class LinkNode {
    val: number
    pre: LinkNode
    nxt: LinkNode
    constructor(val: number, pre: LinkNode = null, nxt: LinkNode = null) {
        this.val = val
        this.pre = pre
        this.nxt = nxt
    }

    addRight(node: LinkNode) {
        node.nxt = this.nxt
        if (node.nxt != null) {
            node.nxt.pre = node
        }
        this.nxt = node
        node.pre = this
    }

    delRight() {
        this.nxt = this.nxt.nxt
        if (this.nxt != null) {
            this.nxt.pre = this
        }
    }
}
class MyLinkedList {
    size: number
    head: LinkNode
    tail: LinkNode

    constructor() {
        this.size = 0
        this.head = new LinkNode(-1)
        this.tail = new LinkNode(-1, this.head)
        this.head.nxt = this.tail
    }

    getNode(index: number): LinkNode {
        if (index < 0 || index >= this.size) {
            return null
        }
        let node: LinkNode
        if (index * 2 > this.size) {
            node = this.tail
            for (let i = 0; i < this.size - index; i++) {
                node = node.pre
            }
        } else {
            node = this.head
            for (let i = 0; i <= index; i++) {
                node = node.nxt
            }
        }
        return node
    }

    get(index: number): number {
        const node: LinkNode = this.getNode(index)
        return node == null ? -1: node.val
    }

    addAtHead(val: number): void {
        this.head.addRight(new LinkNode(val))
        this.size++
    }

    addAtTail(val: number): void {
        this.tail.pre.addRight(new LinkNode(val))
        this.size++
    }

    addAtIndex(index: number, val: number): void {
        if(index <= this.size) {
            if (index <= 0) {
                this.addAtHead(val)
            } else if (index == this.size) {
                this.addAtTail(val)
            } else {
                this.getNode(index).pre.addRight(new LinkNode(val))
                this.size++
            }
        }
    }

    deleteAtIndex(index: number): void {
        const node: LinkNode = this.getNode(index)
        if (node != null) {
            node.pre.delRight()
            this.size--
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```
```Go []
type LinkNode struct {
    Val int
    Pre, Nxt *LinkNode
}

func ConstructLinkNode(val int, pre *LinkNode, nxt *LinkNode) LinkNode {
    return LinkNode{val, pre, nxt}
}

func (this *LinkNode) AddRight(node LinkNode) {
    node.Nxt = this.Nxt
    if node.Nxt != nil {
        node.Nxt.Pre = &node
    }
    this.Nxt = &node
    node.Pre = this
}

func (this *LinkNode) DelRight() {
    this.Nxt = this.Nxt.Nxt
    if this.Nxt != nil {
        this.Nxt.Pre = this
    }
}

type MyLinkedList struct {
    Size int
    Head, Tail *LinkNode
}


func Constructor() MyLinkedList {
    head := ConstructLinkNode(-1, nil, nil)
    tail := ConstructLinkNode(-1, &head, nil)
    head.Nxt = &tail
    return MyLinkedList{0, &head, &tail}
}

func (this *MyLinkedList) GetNode(index int) *LinkNode {
    if index < 0 || index >= this.Size {
        return nil
    }
    var node *LinkNode
    if index > this.Size / 2 {
        node = this.Tail
        for i := 0; i < this.Size - index; i++ {
            node = node.Pre
        }
    } else {
        node = this.Head
        for i := 0; i <= index; i++ {
            node = node.Nxt
        }
    }
    return node
}

func (this *MyLinkedList) Get(index int) int {
    if node := this.GetNode(index); node != nil {
        return node.Val 
    }
    return -1
}


func (this *MyLinkedList) AddAtHead(val int)  {
    this.Head.AddRight(ConstructLinkNode(val, nil, nil))
    this.Size++
}


func (this *MyLinkedList) AddAtTail(val int)  {
    this.Tail.Pre.AddRight(ConstructLinkNode(val, nil, nil))
    this.Size++
}


func (this *MyLinkedList) AddAtIndex(index int, val int)  {
    if index <= this.Size {
        if index <= 0 {
            this.AddAtHead(val)
        } else if index == this.Size {
            this.AddAtTail(val)
        } else {
            this.GetNode(index).Pre.AddRight(ConstructLinkNode(val, nil, nil))
            this.Size++
        }
    }
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
    if node := this.GetNode(index); node != nil {
        node.Pre.DelRight()
        this.Size--
    }
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
```