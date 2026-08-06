# [Python/Java/TypeScript/Go] 动态开点含懒标记线段树模版

> slug: by-himymben-vo9g
> date: 2022-06-19
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Range Module (range-module)
> url: https://leetcode.cn/problems/range-module/solutions/jFax8Z/by-himymben-vo9g/

---
### 解题思路
题目描述的就是一个线段树……

### 代码

```Python3 []
MAX_RANGE = int(1e9 + 7)
class RangeModule:

    def __init__(self):
        self.st = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, 1, MAX_RANGE, left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return SegmentTree.query(self.st.root, 1, MAX_RANGE, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, 1, MAX_RANGE, left, right - 1, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = False

class SegmentTree:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: bool) -> None:
        if l <= lc and rc <= r:
            node.val = v
            # 注意产生变化懒标记就为True，因为更新有删除
            node.add = True
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)
 
    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> bool:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, True
        if l <= mid:
            ans = ans and SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = ans and SegmentTree.query(node.rs, mid + 1, rc, l, r)
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
        node.ls.val, node.rs.val = node.val, node.val
        # 注意产生变化懒标记就为True，因为更新有删除
        node.ls.add, node.rs.add = True, True
        node.add = False
    
    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为两者都true
        node.val = node.ls.val and node.rs.val
```
```Java []
class RangeModule {
    private static final int MAX_RANGE = (int)1e9 + 7;
    private SegmentTree sg;
    public RangeModule() {
        sg = new SegmentTree();
    }
    
    public void addRange(int left, int right) {
        sg.update(sg.root, 1, MAX_RANGE, left, right - 1, true);
    }
    
    public boolean queryRange(int left, int right) {
        return sg.query(sg.root, 1, MAX_RANGE, left, right - 1);
    }
    
    public void removeRange(int left, int right) {
        sg.update(sg.root, 1, MAX_RANGE, left, right - 1, false);
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */

 class SegmentTree {
    public Node root;
    public SegmentTree() {
        root = new Node();
    }

    public void update(Node node, int lc, int rc, int l, int r, boolean v) {
        if (l <= lc && rc <= r) {
            node.val = v;
            node.add = true;
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

    public boolean query(Node node, int lc, int rc, int l, int r) {
        if (l <= lc && rc <= r) {
            return node.val;
        }
        pushdown(node);
        int mid = lc + rc >> 1;
        boolean ans = true;
        if (l <= mid) {
            ans = ans && query(node.ls, lc, mid, l, r);
        }
        if (r > mid) {
            ans = ans && query(node.rs, mid + 1, rc, l, r);
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
        if (!node.add) {
            return;
        }
        node.ls.val = node.rs.val = node.val; 
        node.ls.add = node.rs.add = true;
        node.add = false;
    }

    private void pushup(Node node) {
        node.val = node.ls.val && node.rs.val;
    }

    public class Node {
        public Node ls, rs;
        public boolean val, add;
        public Node() {
            val = add = false;
        }
    }
}
```
```TypeScript []
const MAX_RANGE = 1e9 + 7

class RangeModule {
    st: SegmentTree
    constructor() {
        this.st = new SegmentTree()
    }

    addRange(left: number, right: number): void {
        this.st.update(this.st.root, 1, MAX_RANGE, left, right - 1, true)
    }

    queryRange(left: number, right: number): boolean {
        return this.st.query(this.st.root, 1, MAX_RANGE, left, right - 1)
    }

    removeRange(left: number, right: number): void {
        this.st.update(this.st.root, 1, MAX_RANGE, left, right - 1, false)
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * var obj = new RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */

 class SegNode {
    ls: SegNode
    rs: SegNode
    val: boolean
    add: boolean

    constructor() {
        this.ls = this.rs = null
        this.val = this.add = false
    }
}

class SegmentTree {
    root: SegNode
 
    constructor() { 
        this.root = new SegNode()
    }

    update(node: SegNode, lc: number, rc: number, l: number, r: number, v: boolean): void {
        if (l <= lc && rc <= r) {
            node.val = v
            node.add = true
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

    query(node: SegNode, lc: number, rc: number, l: number, r: number): boolean {
        if (l <= lc && rc <= r) {
            return node.val
        }
        this.pushdown(node)
        let ans = true
        const mid = lc + rc >> 1
        if (l <= mid) {
            ans = ans && this.query(node.ls, lc, mid, l, r)
        }
        if (r > mid) {
            ans = ans && this.query(node.rs, mid + 1, rc, l, r)
        }
        return ans
    }

    pushup(node: SegNode): void {
        node.val = node.ls.val && node.rs.val
    }

    pushdown(node: SegNode): void {
        if (node.ls == null) {
            node.ls = new SegNode()
        }
        if (node.rs == null) {
            node.rs = new SegNode()
        }
        if (!node.add) {
            return
        }
        node.ls.add = node.rs.add = true
        node.ls.val = node.rs.val = node.val
        node.add = false
    }
}
```
```Go []
const MAX_RANGE = 1000000009
type RangeModule struct {
    Root *SegmentNode
}


func Constructor() RangeModule {
    return RangeModule{&SegmentNode{nil, nil, false, false}}
}


func (this *RangeModule) AddRange(left int, right int)  {
    this.Root.update(1, MAX_RANGE, left, right - 1, true)
}


func (this *RangeModule) QueryRange(left int, right int) bool {
    return this.Root.query(1, MAX_RANGE, left, right - 1)
}


func (this *RangeModule) RemoveRange(left int, right int)  {
    this.Root.update(1, MAX_RANGE, left, right - 1, false)
}


/**
 * Your RangeModule object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRange(left,right);
 * param_2 := obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */

 type SegmentNode struct {
    Ls, Rs *SegmentNode
    Val, Add bool
}

func (node *SegmentNode) update(lc int, rc int, l int, r int, v bool) {
    if l <= lc && rc <= r {
        node.Val, node.Add = v, true
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

func (node *SegmentNode) query(lc int, rc int, l int, r int) bool {
    if l <= lc && rc <= r {
        return node.Val
    }
    node.pushdown()
    mid, ans := (lc + rc) >> 1, true
    if l <= mid {
        ans = ans && node.Ls.query(lc, mid, l, r)
    }
    if r > mid {
        ans = ans && node.Rs.query(mid + 1, rc, l, r)
    }
    return ans
}

func (node *SegmentNode) pushup() {
    node.Val = node.Ls.Val && node.Rs.Val
}

func (node *SegmentNode) pushdown() {
    if node.Ls == nil {
        node.Ls = &SegmentNode{nil, nil, false, false}
    }
    if node.Rs == nil {
        node.Rs = &SegmentNode{nil, nil, false, false}
    }
    if !node.Add {
        return
    }
    node.Ls.Val, node.Ls.Add, node.Rs.Val, node.Rs.Add = node.Val, true, node.Val, true
    node.Add = false
}
```