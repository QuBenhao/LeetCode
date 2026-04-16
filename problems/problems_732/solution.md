# [Python/Java/TypeScript/Go] 动态开点线段树

> Author: Benhao
> Date: 2022-06-05
> Upvotes: 29
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
直接就是[叶总](https://leetcode.cn/problems/my-calendar-iii/solution/by-ac_oier-cv31/)那儿一个板子的学习😂

### 代码

```Python3 []
class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0

class SegmentTree:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.add += v
            node.val += v
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)
 
    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, 0
        if l <= mid:
            ans = SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, rc, l, r))
        return ans
    
    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.add += node.add
        node.rs.add += node.add
        node.ls.val += node.add
        node.rs.val += node.add
        node.add = 0
    
    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        node.val = max(node.ls.val, node.rs.val)


class MyCalendarThree:

    def __init__(self):
        self.st = SegmentTree()
        self.max_range = int(1e9)

    def book(self, start: int, end: int) -> int:
        SegmentTree.update(self.st.root, 0, self.max_range, start, end - 1, 1)
        return SegmentTree.query(self.st.root, 0, self.max_range, 0, self.max_range)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```
```Java []
class SegmentTree {
    public Node root;
    public SegmentTree() {
        root = new Node();
    }

    public void update(Node node, int lc, int rc, int l, int r, int v) {
        if (l <= lc && rc <= r) {
            node.val += v;
            node.add += v;
            return;
        }
        pushdown(node);
        int mid = lc + rc >> 1;
        if (l <= mid) {
            update(node.ls, lc, mid, l, r, v);
        } 
        if (r > mid) {
            update(node.rs, mid + 1, rc, l, r, v);
        }
        pushup(node);
    }

    public int query(Node node, int lc, int rc, int l, int r) {
        if (l <= lc && rc <= r) {
            return node.val;
        }
        pushdown(node);
        int ans = 0, mid = lc + rc >> 1;
        if (l <= mid) {
            ans = query(node.ls, lc, mid, l, r);
        }
        if (r > mid) {
            ans = Math.max(ans, query(node.rs, mid + 1, rc, l, r));
        }
        return ans;
    }

    private void pushdown(Node node) {
        if (node.ls == null) {
            node.ls = new Node();
        }
        if (node.rs == null) {
            node.rs = new Node();
        }
        if (node.add == 0) {
            return;
        }
        node.ls.val += node.add;
        node.ls.add += node.add;
        node.rs.val += node.add;
        node.rs.add += node.add;
        node.add = 0;
    }

    private void pushup(Node node) {
        node.val = Math.max(node.ls.val, node.rs.val);
    }

    public class Node {
        public Node ls, rs;
        public int val, add;
        public Node() {
            val = add = 0;
        }
    }
}

class MyCalendarThree {
    private SegmentTree sg;
    private static final int MAX_RANGE = (int)1e9;
    public MyCalendarThree() {
        sg = new SegmentTree();
    }
    
    public int book(int start, int end) {
        sg.update(sg.root, 0, MAX_RANGE, start, end - 1, 1);
        return sg.query(sg.root, 0, MAX_RANGE, 0, MAX_RANGE);
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */
```
```TypeScript []
class SegNode {
    ls: SegNode
    rs: SegNode
    val: number
    add: number

    constructor() {
        this.ls = this.rs = null
        this.val = this.add = 0
    }
}

class SegmentTree {
    root: SegNode
 
    constructor() { 
        this.root = new SegNode()
    }

    update(node: SegNode, lc: number, rc: number, l: number, r: number, v: number): void {
        if (l <= lc && rc <= r) {
            node.val += v
            node.add += v
            return
        }
        this.pushdown(node)
        const mid = lc + rc >> 1
        if (l <= mid) {
            this.update(node.ls, lc, mid, l, r, v)
        }
        if (r > mid) {
            this.update(node.rs, mid + 1, rc, l, r, v)
        }
        this.pushup(node)
    }

    query(node: SegNode, lc: number, rc: number, l: number, r: number): number {
        if (l <= lc && rc <= r) {
            return node.val
        }
        this.pushdown(node)
        let ans = 0
        const mid = lc + rc >> 1
        if (l <= mid) {
            ans = this.query(node.ls, lc, mid, l, r)
        }
        if (r > mid) {
            ans = Math.max(ans, this.query(node.rs, mid + 1, rc, l, r))
        }
        return ans
    }

    pushup(node: SegNode): void {
        node.val = Math.max(node.ls.val, node.rs.val)
    }

    pushdown(node: SegNode): void {
        if (node.ls == null) {
            node.ls = new SegNode()
        }
        if (node.rs == null) {
            node.rs = new SegNode()
        }
        if (node.add == 0) {
            return
        }
        node.ls.add += node.add
        node.ls.val += node.add
        node.rs.add += node.add
        node.rs.val += node.add
        node.add = 0
    }
}

class MyCalendarThree {
    maxRange: number
    sg: SegmentTree
    constructor() {
        this.maxRange = 1e9
        this.sg = new SegmentTree()
    }

    book(start: number, end: number): number {
        this.sg.update(this.sg.root, 0, this.maxRange, start, end - 1, 1)
        return this.sg.query(this.sg.root, 0, this.maxRange, 0, this.maxRange)
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(start,end)
 */
```
```Go []
type SegmentNode struct {
    Ls, Rs *SegmentNode
    Val, Add int
}

func (node *SegmentNode) update(lc int, rc int, l int, r int, v int) {
    if l <= lc && rc <= r {
        node.Val += v
        node.Add += v
        return
    }
    node.pushdown()
    mid := (lc + rc) >> 1
    if l <= mid {
        node.Ls.update(lc, mid, l, r, v)
    }
    if r > mid {
        node.Rs.update(mid + 1, rc, l, r, v)
    }
    node.pushup()
}

func (node *SegmentNode) query(lc int, rc int, l int, r int) (ans int) {
    if l <= lc && rc <= r {
        return node.Val
    }
    node.pushdown()
    mid := (lc + rc) >> 1
    if l <= mid {
        ans = node.Ls.query(lc, mid, l, r)
    }
    if r > mid {
        ans = max(ans, node.Rs.query(mid + 1, rc, l, r))
    }
    return
}

func (node *SegmentNode) pushup() {
    node.Val = max(node.Ls.Val, node.Rs.Val)
}

func (node *SegmentNode) pushdown() {
    if node.Ls == nil {
        node.Ls = &SegmentNode{nil, nil, 0, 0}
    }
    if node.Rs == nil {
        node.Rs = &SegmentNode{nil, nil, 0, 0}
    }
    if node.Add == 0 {
        return
    }
    node.Ls.Val += node.Add
    node.Ls.Add += node.Add
    node.Rs.Val += node.Add
    node.Rs.Add += node.Add
    node.Add = 0
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

const MAX_RANGE int = 1_000_000_000

type MyCalendarThree struct {
    Root SegmentNode
}


func Constructor() MyCalendarThree {
    return MyCalendarThree{SegmentNode{}}
}


func (this *MyCalendarThree) Book(start int, end int) int {
    this.Root.update(0, MAX_RANGE, start, end - 1, 1)
    return this.Root.query(0, MAX_RANGE, 0, MAX_RANGE)
}


/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
```