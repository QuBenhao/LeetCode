# [Python/Java/JavaScript/Go] 双向链表 + 哈希表

> slug: python-bu-man-zu-yao-qiu-jin-by-himymben-4zs4
> date: 2022-03-15
> tags: Go, Java, JavaScript, Python, Python3
> question: All O`one Data Structure (all-oone-data-structure)
> url: https://leetcode.cn/problems/all-oone-data-structure/solutions/hThtMA/python-bu-man-zu-yao-qiu-jin-by-himymben-4zs4/

---
### 解题思路
记录每个字母映射到的双向链表中的节点，节点中包括统计的数量信息。
维护最左和最右的链表节点就可以O(1)返回最大值、最小值。

（Python以外为复制的代码，仅做记录）

### 代码

```Python3 []
class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.strs = set()
        self.prev = None
        self.next = None
    
    def add(self, s):
        self.strs.add(s)
    
    def remove(self, s):
        self.strs.remove(s)

class AllOne:

    def __init__(self):
        self.nodes = dict()
        self.max = self.min = None

    def inc(self, key: str) -> None:
        if key in self.nodes:
            oldNode = self.nodes[key]
            oldNode.remove(key)
            if oldNode.next and oldNode.next.cnt == oldNode.cnt + 1:
                oldNode.next.add(key)
                self.nodes[key] = oldNode.next
            else:
                node = Node(oldNode.cnt + 1)
                if node.cnt > self.max.cnt:
                    self.max = node
                self.nodes[key] = node
                node.add(key)
                node.next = oldNode.next
                if node.next:
                    node.next.prev = node
                node.prev = oldNode
                oldNode.next = node
            if not oldNode.strs:
                if oldNode.prev:
                    oldNode.prev.next = oldNode.next
                else:
                    self.min = oldNode.next
                if oldNode.next:
                    oldNode.next.prev = oldNode.prev
                else:
                    self.max = oldNode.prev
        else:
            if self.min and self.min.cnt == 1:
                self.nodes[key] = self.min
                self.min.add(key)
            else:
                node = Node(1)
                node.add(key)
                self.nodes[key] = node
                node.next = self.min
                if self.min:
                    self.min.prev = node
                self.min = node
                if not self.max:
                    self.max = node

    def dec(self, key: str) -> None:
        oldNode = self.nodes[key]
        oldNode.remove(key)
        if oldNode.prev and oldNode.prev.cnt == oldNode.cnt - 1:
            oldNode.prev.add(key)
            self.nodes[key] = oldNode.prev
        elif oldNode.cnt > 1:
            node = Node(oldNode.cnt - 1)
            self.nodes[key] = node
            node.add(key)
            node.prev = oldNode.prev
            if node.prev:
                node.prev.next = node
            else:
                self.min = node
            node.next = oldNode
            oldNode.prev = node
        if oldNode.cnt == 1:
            self.nodes.pop(key)
        if not oldNode.strs:
            print(key)
            if oldNode.prev:
                oldNode.prev.next = oldNode.next
            else:
                self.min = oldNode.next
            if oldNode.next:
                oldNode.next.prev = oldNode.prev
            else:
                self.max = oldNode.prev

    def getMaxKey(self) -> str:
        if not self.max:
            return ""
        k = self.max.strs.pop()
        self.max.strs.add(k)
        return k

    def getMinKey(self) -> str:
        if not self.min:
            return ""
        k = self.min.strs.pop()
        self.min.strs.add(k)
        return k


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```
```Java []
public class AllOne {

    // use hash alogirthm ensures O(1)
    private Map<String, Node> values;
    // use double-linked list ensures getMax or getMin O(1)
    private Node head;
    private Node tail;

    class Node {

        Node(Node pre, Node next, String key, int value) {
            this.pre = pre;
            this.value = value;
            this.next = next;
            this.key = key;
        }

        private Node pre;
        private Node next;
        private int value;
        private String key;
    }

    public AllOne() {
        this.values = new HashMap<>(8);
    }

    public void inc(String key) {
        Node node = this.values.get(key);
        if (node == null) {
            node = new Node(null, null, key, 1);
            values.put(key, node);
            if (head == null) {
                head = tail = node;
                return;
            }
            Node p = head;
            p.pre = node;
            node.next = p;
            head = node;
        } else {
            node.value++;
            while (node.next != null && node.next.value < node.value) {
                swapNode(node, node.next);
            }
        }
    }

    private void swapNode(Node node1, Node node2) {
        Node node1Pre = node1.pre;
        Node node2Next = node2.next;

        node1.pre = node2;
        node1.next = node2Next;
        node2.next = node1;
        node2.pre = node1Pre;
        if (node1Pre != null) {
            node1Pre.next = node2;
        }
        if (node2Next != null) {
            node2Next.pre = node1;
        }
        if (head == node1) {
            head = node2;
        }
        if (tail == node2) {
            tail = node1;
        }
    }


    public void dec(String key) {
        Node node = this.values.get(key);
        if (node == null) {
            return;
        } else if (node.value == 1) {
            if (node == head) {
                head = node.next;
            }
            if (tail == node) {
                tail = node.pre;
            }
            if (node.pre != null) {
                node.pre.next = node.next;
            }
            if (node.next != null) {
                node.next.pre = node.pre;
            }
        } else {
            node.value--;
            while (node.pre != null && node.pre.value > node.value) {
                swapNode(node.pre, node);
            }
        }
    }

    public String getMaxKey() {
        return tail == null ? "" : tail.key;
    }

    public String getMinKey() {
        return head == null ? "" : head.key;
    }
}

```
```JavaScript []
var AllOne = function() {
    this.root = new Node();
    this.root.prev = this.root;
    this.root.next = this.root; // 初始化链表哨兵，下面判断节点的 next 若为 root，则表示 next 为空（prev 同理）
    this.nodes = new Map();
};

AllOne.prototype.inc = function(key) {
    if (this.nodes.has(key)) {
        const cur = this.nodes.get(key);
        const nxt = cur.next;
        if (nxt === this.root || nxt.count > cur.count + 1) {
            this.nodes.set(key, cur.insert(new Node(key, cur.count + 1)));
        } else {
            nxt.keys.add(key);
            this.nodes.set(key, nxt);
        }
        cur.keys.delete(key);
        if (cur.keys.size === 0) {
            cur.remove();
        }
    } else {  // key 不在链表中
        if (this.root.next === this.root || this.root.next.count > 1) {
            this.nodes.set(key, this.root.insert(new Node(key, 1)));
        } else {
            this.root.next.keys.add(key);
            this.nodes.set(key, this.root.next);
        }
    }    
};

AllOne.prototype.dec = function(key) {
    const cur = this.nodes.get(key);
    if (cur.count === 1) {  // key 仅出现一次，将其移出 nodes
        this.nodes.delete(key);
    } else {
        const pre = cur.prev;
        if (pre === this.root || pre.count < cur.count - 1) {
            this.nodes.set(key, cur.prev.insert(new Node(key, cur.count - 1)));
        } else {
            pre.keys.add(key);
            this.nodes.set(key, pre);
        }
    }
    cur.keys.delete(key);
    if (cur.keys.size === 0) {
        cur.remove();
    }
};

AllOne.prototype.getMaxKey = function() {
    if (!this.root.prev) {
        return "";
    }
    let maxKey = "";
    for (const key of this.root.prev.keys) {
        maxKey = key;
        break;
    }
    return maxKey;
};

AllOne.prototype.getMinKey = function() {
    if (!this.root.next) {
        return "";
    }
    let minKey = "";
    for (const key of this.root.next.keys) {
        minKey = key;
        break;
    }
    return minKey;
};

class Node {
    constructor(key, count) {
        count ? this.count = count : 0;
        this.keys = new Set();
        key ? this.keys.add(key) : this.keys.add("");
    }

    insert(node) {  // 在 this 后插入 node
        node.prev = this;
        node.next = this.next;
        node.prev.next = node;
        node.next.prev = node;
        return node;
    }

    remove() {
        this.prev.next = this.next;
        this.next.prev = this.prev;
    }
}
```
```Go []
// github.com/EndlessCheng/codeforces-go
type AllOne struct{}

type node struct {
    set map[string]struct{}
    cnt int
}

var lst *list.List
var es map[string]*list.Element

func Constructor() (_ AllOne) {
    lst = list.New()
    es = map[string]*list.Element{}
    return
}

func (AllOne) Inc(key string) {
    if e := es[key]; e != nil {
        cur := e.Value.(node)
        if nxt := e.Next(); nxt == nil || nxt.Value.(node).cnt != cur.cnt+1 {
            es[key] = lst.InsertAfter(node{map[string]struct{}{key: {}}, cur.cnt + 1}, e)
        } else {
            nxt.Value.(node).set[key] = struct{}{}
            es[key] = nxt
        }
        delete(cur.set, key)
        if len(cur.set) == 0 {
            lst.Remove(e)
        }
    } else {
        if lst.Front() == nil || lst.Front().Value.(node).cnt > 1 {
            es[key] = lst.PushFront(node{map[string]struct{}{key: {}}, 1})
        } else {
            lst.Front().Value.(node).set[key] = struct{}{}
            es[key] = lst.Front()
        }
    }
}

func (AllOne) Dec(key string) {
    e := es[key]
    cur := e.Value.(node)
    if cur.cnt > 1 {
        if pre := e.Prev(); pre == nil || pre.Value.(node).cnt != cur.cnt-1 {
            es[key] = lst.InsertBefore(node{map[string]struct{}{key: {}}, cur.cnt - 1}, e)
        } else {
            pre.Value.(node).set[key] = struct{}{}
            es[key] = pre
        }
    } else {
        delete(es, key)
    }
    delete(cur.set, key)
    if len(cur.set) == 0 {
        lst.Remove(e)
    }
}

func (AllOne) GetMaxKey() string {
    if b := lst.Back(); b != nil {
        for s := range b.Value.(node).set {
            return s
        }
    }
    return ""
}

func (AllOne) GetMinKey() string {
    if f := lst.Front(); f != nil {
        for s := range f.Value.(node).set {
            return s
        }
    }
    return ""
}
func init() { debug.SetGCPercent(-1) }
```