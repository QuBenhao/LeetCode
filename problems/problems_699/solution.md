# [Python/Java/TypeScript/Go] 映射暴力 -> 线段树

> Author: Benhao
> Date: 2022-05-26
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
先用Py实现一个映射暴力解，效率很高😂

从三叶那里学了一下【线段树动态开点 + 懒标记】的写法

内心OS：
五月一整个月的每日怎么感觉都挺难写的

### 代码

```python3
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        pos = set()
        for a, length in positions:
            pos.add(a)
            pos.add(a + length - 1)
        idx_map = {v: i for i, v in enumerate(sorted(pos))}
        records = [0] * len(idx_map)
        ans, cur = [], 0
        for a, length in positions:
            left, right = idx_map[a], idx_map[a + length - 1]
            new_height = max(records[left:right + 1]) + length
            for i in range(left, right + 1):
                records[i] = new_height
            cur = max(cur, new_height)
            ans.append(cur)
        return ans
```

从[叶总](https://leetcode.cn/problems/falling-squares/solution/by-ac_oier-zpf0/)那儿抄一套带懒标记的动态开点线段树
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
            node.add = v
            node.val = v
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
        node.ls.add, node.rs.add, node.ls.val, node.rs.val = [node.add] * 4
        node.add = 0
    
    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        node.val = max(node.ls.val, node.rs.val)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans, st, max_range = [], SegmentTree(), int(1e9)
        for a, length in positions:
            SegmentTree.update(st.root, 0, max_range, a, a + length - 1, SegmentTree.query(st.root, 0, max_range, a, a + length - 1) + length)
            ans.append(st.root.val)
        return ans
```
```Java []
class SegmentTree {
    public Node root;
    public SegmentTree() {
        root = new Node();
    }

    public void update(Node node, int lc, int rc, int l, int r, int v) {
        if (l <= lc && rc <= r) {
            node.val = v;
            node.add = v;
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
        node.ls.val = node.ls.add = node.rs.val = node.rs.add = node.add;
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

class Solution {
    private static final int MAX_RANGE = (int)1e9;
    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> ans = new ArrayList<>();
        SegmentTree st = new SegmentTree();
        for(int[] pos: positions) {
            int left = pos[0], right = pos[0] + pos[1] - 1;
            int cur = st.query(st.root, 0, MAX_RANGE, left, right);
            st.update(st.root, 0, MAX_RANGE, left, right, cur + pos[1]);
            ans.add(st.root.val);
        }
        return ans;
    }
}
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
            node.val = node.add = v
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
        node.ls.add = node.ls.val = node.rs.add = node.rs.val = node.add
        node.add = 0
    }
}

const MAX_RANGE = 1e9
function fallingSquares(positions: number[][]): number[] {
    const st = new SegmentTree(), ans = new Array()
    for(const [left, length] of positions) {
        const right = left + length - 1
        const cur = st.query(st.root, 0, MAX_RANGE, left, right)
        st.update(st.root, 0, MAX_RANGE, left, right, cur + length)
        ans.push(st.root.val)
    }
    return ans
};
```
```Go []
type SegmentNode struct {
    Ls, Rs *SegmentNode
    Val, Add int
}

func (node *SegmentNode) update(lc int, rc int, l int, r int, v int) {
    if l <= lc && rc <= r {
        node.Val, node.Add = v, v
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
    node.Ls.Val, node.Ls.Add, node.Rs.Val, node.Rs.Add = node.Add, node.Add, node.Add, node.Add
    node.Add = 0
}

func fallingSquares(positions [][]int) (ans []int) {
    root, MAX_RANGE := &SegmentNode{nil, nil, 0, 0}, 1_000_000_000
    for _, pos := range positions {
        left, right := pos[0], pos[0] + pos[1] - 1
        cur := root.query(0, MAX_RANGE, left, right)
        root.update(0, MAX_RANGE, left, right, cur + pos[1])
        ans = append(ans, root.Val)
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```