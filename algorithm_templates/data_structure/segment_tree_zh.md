# 线段树

线段树是一种二叉树数据结构，用于高效解决**区间查询**（如区间求和、最大值、最小值）和**单点/区间更新**问题。时间复杂度为 O(log
n)。

- 核心思想
    - 结构：每个节点代表一个区间，叶子节点代表单个元素，内部节点合并子区间的信息。
    - 分治：将区间不断二分，直到不可分割。
    - 合并：父节点存储子节点信息的聚合值（如求和、最大值等）。

- 线段树操作
    - 构建：递归分割区间，计算初始值。
    - 查询：分解目标区间，合并覆盖区间的结果。
    - 更新：更新叶子节点，回溯更新父节点。

| 类型      | 空间复杂度      | 使用场景             |
|---------|------------|------------------|
| 常规线段树   | O(4n)      | 区间较小（如 n ≤ 1e6）  |
| 动态开点线段树 | O(Q log R) | 区间极大（如 R = 1e18） |

## 常规线段树

```python
class SegmentTree:
    def __init__(self, _data):
        self.n = len(_data)
        self.tree = [0] * (4 * self.n)  # 预分配4倍空间
        self.build(0, 0, self.n - 1, _data)

    def build(self, node, start, end, _data):
        """ 递归构建线段树 """
        if start == end:
            self.tree[node] = _data[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self.build(left_node, start, mid, _data)
            self.build(right_node, mid + 1, end, _data)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index, value):
        """ 更新元素 """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if index <= mid:
                self._update(left_node, start, mid, index, value)
            else:
                self._update(right_node, mid + 1, end, index, value)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query_range(self, l, r):
        """ 区间查询 """
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0  # 无交集
        if l <= start and end <= r:
            return self.tree[node]  # 完全覆盖
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        return self._query(left_node, start, mid, l, r) + self._query(right_node, mid + 1, end, l, r)


# 使用示例
data = [1, 3, 5, 7, 9, 11]
st = SegmentTree(data)
print(st.query_range(1, 3))  # 输出 15 (3+5+7)
st.update(2, 10)  # 更新索引2为10
print(st.query_range(1, 3))  # 输出 20 (3+10+7)
```

```go
package main

import "fmt"

type SegmentTree struct {
    tree []int
    n    int
}

func NewSegmentTree(data []int) *SegmentTree {
    n := len(data)
    st := &SegmentTree{
        tree: make([]int, 4*n), // 预分配4倍空间
        n:    n,
    }
    st.build(0, 0, n-1, data)
    return st
}

func (st *SegmentTree) build(node, start, end int, data []int) {
    if start == end {
        st.tree[node] = data[start]
    } else {
        mid := (start + end) / 2
        leftNode := 2*node + 1
        rightNode := 2*node + 2
        st.build(leftNode, start, mid, data)
        st.build(rightNode, mid+1, end, data)
        st.tree[node] = st.tree[leftNode] + st.tree[rightNode]
    }
}

func (st *SegmentTree) Update(index, value int) {
    st.update(0, 0, st.n-1, index, value)
}

func (st *SegmentTree) update(node, start, end, index, value int) {
    if start == end {
        st.tree[node] = value
    } else {
        mid := (start + end) / 2
        leftNode := 2*node + 1
        rightNode := 2*node + 2
        if index <= mid {
            st.update(leftNode, start, mid, index, value)
        } else {
            st.update(rightNode, mid+1, end, index, value)
        }
        st.tree[node] = st.tree[leftNode] + st.tree[rightNode]
    }
}

func (st *SegmentTree) QueryRange(l, r int) int {
    return st.query(0, 0, st.n-1, l, r)
}

func (st *SegmentTree) query(node, start, end, l, r int) int {
    if r < start || end < l {
        return 0 // 无交集
    }
    if l <= start && end <= r {
        return st.tree[node] // 完全覆盖
    }
    mid := (start + end) / 2
    leftNode := 2*node + 1
    rightNode := 2*node + 2
    return st.query(leftNode, start, mid, l, r) + st.query(rightNode, mid+1, end, l, r)
}

func main() {
    data := []int{1, 3, 5, 7, 9, 11}
    st := NewSegmentTree(data)
    fmt.Println(st.QueryRange(1, 3)) // 输出 15
    st.Update(2, 10)
    fmt.Println(st.QueryRange(1, 3)) // 输出 20
}
```

## 动态开点

动态开点线段树（惰性建树）适用于区间范围极大（如 $`10^9`$）但实际操作稀疏的场景，通过按需创建节点节省内存。

- **动态开点线段树原理**

延迟初始化：仅在访问时创建子节点。

节点管理：每个节点保存左右子节点指针和区间聚合值。

节省空间：空间复杂度由操作次数决定，而非数据范围。

```python
class Node:
    __slots__ = ['left', 'right', 'val', 'lazy']  # 优化内存

    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0  # 惰性标记（用于区间更新）


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end  # 区间右端点

    def _push_down(self, node, l, r):
        # 动态创建子节点并下推惰性标记
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:
            mid = (l + r) // 2
            # 更新左子节点
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            # 更新右子节点
            node.right.val += node.lazy * (r - mid)
            node.right.lazy += node.lazy
            node.lazy = 0

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:  # 完全覆盖
            node.val += val * (r - l + 1)
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.val = node.left.val + node.right.val

    def update_range(self, l, r, val):
        """区间更新 [l, r] 增加 val"""
        self._update(self.root, self.start, self.end, l, r, val)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return self._query(node.left, l, mid, ql, qr) + self._query(node.right, mid + 1, r, ql, qr)

    def query_range(self, l, r):
        """查询区间 [l, r] 的和"""
        return self._query(self.root, self.start, self.end, l, r)


# 使用示例（假设区间范围为 [0, 1e9]）
dst = DynamicSegmentTree(0, 10 ** 9)
dst.update_range(1, 3, 5)  # 区间 [1,3] 增加5
print(dst.query_range(2, 4))  # 输出 5（仅覆盖到3）
```

```go
package main

import "fmt"

type Node struct {
    left, right *Node
    val, lazy   int
}

type DynamicSegmentTree struct {
    root        *Node
    start, end  int
}

func NewDynamicSegmentTree(start, end int) *DynamicSegmentTree {
    return &DynamicSegmentTree{
        root:  &Node{},
        start: start,
        end:   end,
    }
}

func (dst *DynamicSegmentTree) pushDown(node *Node, l, r int) {
    if node.left == nil {
        node.left = &Node{}
    }
    if node.right == nil {
        node.right = &Node{}
    }
    if node.lazy != 0 {
        mid := (l + r) / 2
        // 更新左子节点
        node.left.val += node.lazy * (mid - l + 1)
        node.left.lazy += node.lazy
        // 更新右子节点
        node.right.val += node.lazy * (r - mid)
        node.right.lazy += node.lazy
        node.lazy = 0
    }
}

func (dst *DynamicSegmentTree) update(node *Node, l, r, ul, ur, val int) {
    if ul <= l && r <= ur {
        node.val += val * (r - l + 1)
        node.lazy += val
        return
    }
    dst.pushDown(node, l, r)
    mid := (l + r) / 2
    if ul <= mid {
        dst.update(node.left, l, mid, ul, ur, val)
    }
    if ur > mid {
        dst.update(node.right, mid+1, r, ul, ur, val)
    }
    node.val = node.left.val + node.right.val
}

func (dst *DynamicSegmentTree) UpdateRange(l, r, val int) {
    dst.update(dst.root, dst.start, dst.end, l, r, val)
}

func (dst *DynamicSegmentTree) query(node *Node, l, r, ql, qr int) int {
    if qr < l || r < ql {
        return 0
    }
    if ql <= l && r <= qr {
        return node.val
    }
    dst.pushDown(node, l, r)
    mid := (l + r) / 2
    return dst.query(node.left, l, mid, ql, qr) +
           dst.query(node.right, mid+1, r, ql, qr)
}

func (dst *DynamicSegmentTree) QueryRange(l, r int) int {
    return dst.query(dst.root, dst.start, dst.end, l, r)
}

func main() {
    dst := NewDynamicSegmentTree(0, 1e9)
    dst.UpdateRange(1, 3, 5)
    fmt.Println(dst.QueryRange(2, 4)) // 输出 5
}
```

## 动态指针

- 核心概念

1. **动态指针**：
    - 每个节点保存左右子节点的**指针**（引用），而非固定数组索引。
    - **按需创建子节点**：在首次访问时动态分配内存（通过 `push_down` 实现）。
    - 优点：节省内存，适合处理 `1e18` 级别的稀疏区间操作。

2. **惰性传播 (Lazy Propagation)**：
    - 延迟对子节点的更新操作，通过 `lazy` 标记记录待处理的任务。
    - 在访问子节点前通过 `push_down` 方法将标记下推并更新子节点。

```python
class Node:
    __slots__ = ['left', 'right', 'val', 'lazy']

    def __init__(self):
        self.left = None  # 动态指针：左子节点
        self.right = None  # 动态指针：右子节点
        self.val = 0  # 当前区间的聚合值（根据场景修改初始值）
        self.lazy = 0  # 惰性标记（根据场景定义含义）


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end  # 区间右端点

    def _push_down(self, node, l, r):
        """动态创建子节点并下推惰性标记"""
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:  # 根据场景修改惰性标记处理逻辑
            mid = (l + r) // 2
            # 示例：区间增加值（修改此处实现其他操作）
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            node.right.val += node.lazy * (r - mid)
            node.right.lazy += node.lazy
            node.lazy = 0  # 清除标记

    def _update(self, node, l, r, ul, ur, val):
        """更新区间 [ul, ur]（根据场景修改更新逻辑）"""
        if ul <= l and r <= ur:
            # 示例：区间增加值（修改此处实现其他操作）
            node.val += val * (r - l + 1)
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        # 聚合子节点结果（根据场景修改聚合逻辑）
        node.val = node.left.val + node.right.val

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _query(self, node, l, r, ql, qr):
        """查询区间 [ql, qr]（根据场景修改查询逻辑）"""
        if qr < l or r < ql:
            return 0  # 根据场景返回初始值（如最大值返回 -inf）
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        # 聚合子查询结果（根据场景修改合并逻辑）
        return self._query(node.left, l, mid, ql, qr) + self._query(node.right, mid + 1, r, ql, qr)

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)
```

### 动态指针管理注意事项

1. **内存控制**：
    - 在 Python 中，未被引用的节点会被自动回收；在 Go 中需手动管理（或依赖 GC）。
    - 在极端情况下，可添加节点复用池减少内存分配开销。
2. **递归深度**：
    - 处理极大区间时可能触发栈溢出，可改用迭代实现或调整递归深度限制。
3. **标记下推顺序**：
    - 必须在访问子节点前调用 `push_down`，确保子节点已创建且标记已处理。

### 性能优化技巧

| 技巧        | 适用场景        | 实现方式                     |
|-----------|-------------|--------------------------|
| **节点池复用** | 高频更新/查询操作   | 预分配节点对象池，通过索引管理而非动态创建/销毁 |
| **迭代实现**  | 避免递归栈溢出     | 用栈或队列模拟递归过程              |
| **离散化坐标** | 区间端点稀疏但数量有限 | 将原始坐标映射到紧凑的整数范围，减少动态开点需求 |

### 动态开点线段树应用

线段树的核心逻辑在不同场景下需要调整的部分主要集中在 **聚合方式** 和 **惰性标记处理** 上。以下是关键修改点：

| 场景         | 修改点                                  | 示例（区间求和 → 区间最大值）                      |
|------------|--------------------------------------|---------------------------------------|
| **聚合逻辑**   | 合并子区间结果的方式（如 `sum` → `max`）          | `node.val = max(left.val, right.val)` |
| **惰性标记处理** | 区间更新时的标记传递逻辑（如加减 → 赋值）               | `lazy` 存储待赋值的值而非增量                    |
| **初始化值**   | 根据聚合逻辑选择初始值（如求和初始化为0，最大值初始化为负无穷）     | `self.val = -inf`                     |
| **区间合并方式** | 查询时如何合并部分覆盖区间的结果（如求和直接相加，最大值取子区间最大值） | `return max(left_query, right_query)` |

#### 区间求和

- 场景：求区间内元素的和，支持区间增减操作（如 [l, r] += val）。

```python
class SumSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = 0  # 区间和
            self.lazy = 0  # 延迟增加量

    def __init__(self, start, end):
        self.root = self.Node()
        self.start = start
        self.end = end

    def _push_down(self, node, l, r):
        if node.left is None:
            node.left = self.Node()
        if node.right is None:
            node.right = self.Node()
        if node.lazy != 0:
            mid = (l + r) // 2
            # 更新左子树
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            # 更新右子树
            node.right.val += node.lazy * (r - mid)
            node.right.lazy += node.lazy
            node.lazy = 0

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.val += val * (r - l + 1)
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.val = node.left.val + node.right.val

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0  # 无交集
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return self._query(node.left, l, mid, ql, qr) + self._query(node.right, mid + 1, r, ql, qr)

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)
```

#### 区间最小值

- 场景：求区间内的最小值，支持区间赋值操作（如 [l, r] = val）。

```python
class MinSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = float('inf')  # 初始为无穷大
            self.lazy = None  # 延迟赋值标记

    def __init__(self, start, end):
        self.root = self.Node()
        self.start = start
        self.end = end

    def _push_down(self, node):
        if node.left is None:
            node.left = self.Node()
        if node.right is None:
            node.right = self.Node()
        if node.lazy is not None:
            # 赋值操作覆盖子节点
            node.left.val = node.lazy
            node.left.lazy = node.lazy
            node.right.val = node.lazy
            node.right.lazy = node.lazy
            node.lazy = None

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.val = val  # 直接赋值
            node.lazy = val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.val = min(node.left.val, node.right.val)  # 合并逻辑

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return float('inf')  # 不影响最小值计算
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node)
        mid = (l + r) // 2
        return min(
            self._query(node.left, l, mid, ql, qr),
            self._query(node.right, mid + 1, r, ql, qr)
        )
```

#### 区间最大值

- 场景：求区间内的最大值，支持区间增减操作（如 [l, r] += val）。

```python
class MaxSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'max_val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.max_val = -float('inf')  # 初始为负无穷
            self.lazy = 0  # 延迟增加量

    def __init__(self, start, end):
        self.root = self.Node()
        self.start = start
        self.end = end

    def _push_down(self, node):
        if node.left is None:
            node.left = self.Node()
        if node.right is None:
            node.right = self.Node()
        if node.lazy != 0:
            # 传递增量
            node.left.max_val += node.lazy
            node.left.lazy += node.lazy
            node.right.max_val += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.max_val += val  # 增加最大值
            node.lazy += val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.max_val = max(node.left.max_val, node.right.max_val)  # 合并逻辑

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return -float('inf')  # 不影响最大值计算
        if ql <= l and r <= qr:
            return node.max_val
        self._push_down(node)
        mid = (l + r) // 2
        return max(
            self._query(node.left, l, mid, ql, qr),
            self._query(node.right, mid + 1, r, ql, qr)
        )
```

#### 区间更新

-场景：区间赋值操作，覆盖之前的修改（如 [l, r] = val）。

```python
class RangeAssignSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = 0  # 当前区间的值（全部相同）
            self.lazy = None  # 延迟赋值标记

    def __init__(self, start, end):
        self.root = self.Node()
        self.start = start
        self.end = end

    def _push_down(self, node):
        if node.left is None:
            node.left = self.Node()
        if node.right is None:
            node.right = self.Node()
        if node.lazy is not None:
            # 传递赋值标记
            node.left.val = node.lazy
            node.left.lazy = node.lazy
            node.right.val = node.lazy
            node.right.lazy = node.lazy
            node.lazy = None

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.val = val
            node.lazy = val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)

    def query_point(self, idx):
        return self._query(self.root, self.start, self.end, idx)

    def _query(self, node, l, r, idx):
        if l == r:
            return node.val
        self._push_down(node)
        mid = (l + r) // 2
        if idx <= mid:
            return self._query(node.left, l, mid, idx)
        else:
            return self._query(node.right, mid + 1, r, idx)
```
