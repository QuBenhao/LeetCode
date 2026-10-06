# Segment Tree

A segment tree is a binary tree data structure that efficiently handles **range queries** (such as sums, maxima, and minima) and **point/range updates**, with a time complexity of O(log
n).

- Core ideas
    - Structure: Each node represents a range. Leaves represent individual elements, and internal nodes combine information from their child ranges.
    - Divide and conquer: Repeatedly split a range in half until it cannot be divided further.
    - Merge: A parent stores the aggregate of its children's information, such as a sum or maximum.

- Segment tree operations
    - Build: Recursively divide the range and compute initial values.
    - Query: Split the target range and combine the results from the covered ranges.
    - Update: Update a leaf, then update its ancestors on the way back up.

| Type | Space Complexity | Use Case |
|---------|------------|------------------|
| Standard segment tree | O(4n) | Small ranges (e.g., n ≤ 1e6) |
| Dynamic segment tree | O(Q log R) | Very large ranges (e.g., R = 1e18) |

## Standard Segment Tree

```python
class SegmentTree:
    def __init__(self, _data):
        self.n = len(_data)
        self.tree = [0] * (4 * self.n)  # Preallocate four times the array size
        self.build(0, 0, self.n - 1, _data)

    def build(self, node, start, end, _data):
        """ Build the segment tree recursively. """
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
        """ Update an element. """
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
        """ Range query. """
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0  # No overlap
        if l <= start and end <= r:
            return self.tree[node]  # Fully covered
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        return self._query(left_node, start, mid, l, r) + self._query(right_node, mid + 1, end, l, r)


# Usage example
data = [1, 3, 5, 7, 9, 11]
st = SegmentTree(data)
print(st.query_range(1, 3))  # Outputs 15 (3+5+7)
st.update(2, 10)  # Set index 2 to 10
print(st.query_range(1, 3))  # Outputs 20 (3+10+7)
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
        tree: make([]int, 4*n), // Preallocate four times the array size
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
        return 0 // No overlap
    }
    if l <= start && end <= r {
        return st.tree[node] // Fully covered
    }
    mid := (start + end) / 2
    leftNode := 2*node + 1
    rightNode := 2*node + 2
    return st.query(leftNode, start, mid, l, r) + st.query(rightNode, mid+1, end, l, r)
}

func main() {
    data := []int{1, 3, 5, 7, 9, 11}
    st := NewSegmentTree(data)
    fmt.Println(st.QueryRange(1, 3)) // Outputs 15
    st.Update(2, 10)
    fmt.Println(st.QueryRange(1, 3)) // Outputs 20
}
```

## Dynamic Node Allocation

A dynamic segment tree (built lazily) is useful when the range is very large (e.g., $`10^9`$) but operations are sparse. It saves memory by creating nodes on demand.

- **How a dynamic segment tree works**

Lazy initialization: Create child nodes only when they are accessed.

Node management: Each node stores pointers to its left and right children and the aggregate value for its range.

Space savings: Space complexity depends on the number of operations rather than the size of the value range.

```python
class Node:
    __slots__ = ['left', 'right', 'val', 'lazy']  # Reduce memory usage

    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0  # Lazy tag for range updates


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # Left endpoint of the range
        self.end = end  # Right endpoint of the range

    def _push_down(self, node, l, r):
        # Create child nodes on demand and push down lazy tags
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:
            mid = (l + r) // 2
            # Update the left child
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            # Update the right child
            node.right.val += node.lazy * (r - mid)
            node.right.lazy += node.lazy
            node.lazy = 0

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:  # Fully covered
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
        """Range update: add val to [l, r]."""
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
        """Query the sum over [l, r]."""
        return self._query(self.root, self.start, self.end, l, r)


# Usage example with the range [0, 1e9]
dst = DynamicSegmentTree(0, 10 ** 9)
dst.update_range(1, 3, 5)  # Add 5 to the range [1,3]
print(dst.query_range(2, 4))  # Outputs 5 (covered only up to 3)
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
        // Update the left child
        node.left.val += node.lazy * (mid - l + 1)
        node.left.lazy += node.lazy
        // Update the right child
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
    fmt.Println(dst.QueryRange(2, 4)) // Outputs 5
}
```

## Dynamic Pointers

- Core concepts

1. **Dynamic pointers**:
    - Each node stores **pointers** (references) to its left and right children instead of fixed array indices.
    - **Create children on demand**: Allocate memory dynamically on first access, using `push_down`.
    - Benefit: Saves memory and handles sparse range operations over ranges as large as `1e18`.

2. **Lazy propagation**:
    - Defer updates to children and record pending work in a `lazy` tag.
    - Before accessing children, use `push_down` to propagate the tag and update them.

```python
class Node:
    __slots__ = ['left', 'right', 'val', 'lazy']

    def __init__(self):
        self.left = None  # Dynamic pointer to the left child
        self.right = None  # Dynamic pointer to the right child
        self.val = 0  # Aggregate for the current range; adapt the initial value to the use case
        self.lazy = 0  # Lazy tag; define its meaning for the use case


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # Left endpoint of the range
        self.end = end  # Right endpoint of the range

    def _push_down(self, node, l, r):
        """Create child nodes on demand and push down lazy tags."""
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:  # Adapt lazy tag handling to the use case
            mid = (l + r) // 2
            # Example: Add to a range; change this for other operations
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            node.right.val += node.lazy * (r - mid)
            node.right.lazy += node.lazy
            node.lazy = 0  # Clear the tag

    def _update(self, node, l, r, ul, ur, val):
        """Update [ul, ur]; adapt the update logic to the use case."""
        if ul <= l and r <= ur:
            # Example: Add to a range; change this for other operations
            node.val += val * (r - l + 1)
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        # Aggregate child results; adapt the aggregation logic to the use case
        node.val = node.left.val + node.right.val

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _query(self, node, l, r, ql, qr):
        """Query [ql, qr]; adapt the query logic to the use case."""
        if qr < l or r < ql:
            return 0  # Return the identity value for the use case, e.g., -inf for a maximum
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        # Aggregate subquery results; adapt the merge logic to the use case
        return self._query(node.left, l, mid, ql, qr) + self._query(node.right, mid + 1, r, ql, qr)

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)
```

### Dynamic Pointer Management

1. **Memory management**:
    - Python automatically reclaims unreferenced nodes; in Go, manage them manually or rely on garbage collection.
    - In extreme cases, add a node reuse pool to reduce allocation overhead.
2. **Recursion depth**:
    - Very large ranges may cause a stack overflow. Use an iterative implementation or adjust the recursion limit.
3. **Tag propagation order**:
    - Always call `push_down` before accessing children to ensure they exist and their tags have been processed.

### Performance Optimization Tips

| Technique | Use Case | Implementation |
|-----------|-------------|--------------------------|
| **Node pool reuse** | Frequent updates and queries | Preallocate a pool of nodes and manage them by index instead of creating and destroying them dynamically |
| **Iterative implementation** | Avoid recursion stack overflow | Simulate recursion with a stack or queue |
| **Coordinate compression** | Sparse but finite range endpoints | Map original coordinates to a compact integer range to reduce the need for dynamic node allocation |

### Dynamic Segment Tree Applications

Adapting a segment tree to different use cases mainly involves changing **aggregation** and **lazy tag handling**. The key changes are:

| Aspect | What to Change | Example (Range Sum → Range Maximum) |
|------------|--------------------------------------|---------------------------------------|
| **Aggregation logic** | How child range results are combined (e.g., `sum` → `max`) | `node.val = max(left.val, right.val)` |
| **Lazy tag handling** | How tags propagate during range updates (e.g., addition/subtraction → assignment) | `lazy` stores the value to assign instead of an increment |
| **Initial value** | Choose based on the aggregation logic (e.g., 0 for sums and negative infinity for maxima) | `self.val = -inf` |
| **Combining ranges** | How partially covered query results are merged (e.g., add sums or take the maximum of child ranges) | `return max(left_query, right_query)` |

#### Range Sum

- Use case: Sum the elements in a range, with support for range increments and decrements (e.g., [l, r] += val).

```python
class SumSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = 0  # Range sum
            self.lazy = 0  # Deferred increment

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
            # Update the left subtree
            node.left.val += node.lazy * (mid - l + 1)
            node.left.lazy += node.lazy
            # Update the right subtree
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
            return 0  # No overlap
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return self._query(node.left, l, mid, ql, qr) + self._query(node.right, mid + 1, r, ql, qr)

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)
```

#### Range Minimum

- Use case: Find the minimum in a range, with support for range assignment (e.g., [l, r] = val).

```python
class MinSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = float('inf')  # Initialize to infinity
            self.lazy = None  # Deferred assignment tag

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
            # Overwrite child values with the assignment
            node.left.val = node.lazy
            node.left.lazy = node.lazy
            node.right.val = node.lazy
            node.right.lazy = node.lazy
            node.lazy = None

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.val = val  # Assign directly
            node.lazy = val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.val = min(node.left.val, node.right.val)  # Merge logic

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return float('inf')  # Does not affect the minimum
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node)
        mid = (l + r) // 2
        return min(
            self._query(node.left, l, mid, ql, qr),
            self._query(node.right, mid + 1, r, ql, qr)
        )
```

#### Range Maximum

- Use case: Find the maximum in a range, with support for range increments and decrements (e.g., [l, r] += val).

```python
class MaxSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'max_val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.max_val = -float('inf')  # Initialize to negative infinity
            self.lazy = 0  # Deferred increment

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
            # Propagate the increment
            node.left.max_val += node.lazy
            node.left.lazy += node.lazy
            node.right.max_val += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0

    def update_range(self, l, r, val):
        self._update(self.root, self.start, self.end, l, r, val)

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:
            node.max_val += val  # Increase the maximum
            node.lazy += val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.max_val = max(node.left.max_val, node.right.max_val)  # Merge logic

    def query_range(self, l, r):
        return self._query(self.root, self.start, self.end, l, r)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return -float('inf')  # Does not affect the maximum
        if ql <= l and r <= qr:
            return node.max_val
        self._push_down(node)
        mid = (l + r) // 2
        return max(
            self._query(node.left, l, mid, ql, qr),
            self._query(node.right, mid + 1, r, ql, qr)
        )
```

#### Range Updates

- Use case: Assign values to a range, overwriting earlier updates (e.g., [l, r] = val).

```python
class RangeAssignSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'val', 'lazy']

        def __init__(self):
            self.left = None
            self.right = None
            self.val = 0  # Value of the current range; all elements are equal
            self.lazy = None  # Deferred assignment tag

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
            # Propagate the assignment tag
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
