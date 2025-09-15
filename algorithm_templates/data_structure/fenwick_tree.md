# 树状数组

树状数组（Fenwick Tree）是一种高效处理 **前缀和查询** 和 **单点更新** 的数据结构，时间复杂度为 $`O(\log n)`$。

`子节点t[x]的父节点是t[x+lowbit(x)]`

其中lowbit是求二进制最低位1 (可通过取反，再+1，再&)

```python
class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 索引从1开始

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int) -> None:
        """ 单点更新：a[idx] += delta """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        """ 查询前缀和：a[1] + a[2] + ... + a[idx] """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

    def range_query(self, l: int, r: int) -> int:
        """ 区间查询：a[l] + a[l+1] + ... + a[r] """
        return self.query(r) - self.query(l - 1)


# 示例
arr = [1, 3, 5, 7, 9]
n = len(arr)
ft = FenwickTree(n)
for i in range(1, n + 1):
    ft.update(i, arr[i - 1])

print(ft.query(3))  # 输出9 (1+3+5)
print(ft.range_query(2, 4))  # 输出15 (3+5+7)
```

```go
package main

import "fmt"

type FenwickTree struct {
    n    int
    tree []int
}

func NewFenwickTree(size int) *FenwickTree {
    return &FenwickTree{
        n:    size,
        tree: make([]int, size+1), // 索引从1开始
    }
}

func (ft *FenwickTree) lowbit(x int) int {
    return x & (-x)
}

func (ft *FenwickTree) Update(idx int, delta int) {
    for idx <= ft.n {
        ft.tree[idx] += delta
        idx += ft.lowbit(idx)
    }
}

func (ft *FenwickTree) Query(idx int) int {
    res := 0
    for idx > 0 {
        res += ft.tree[idx]
        idx -= ft.lowbit(idx)
    }
    return res
}

func (ft *FenwickTree) RangeQuery(l, r int) int {
    return ft.Query(r) - ft.Query(l-1)
}

func main() {
    arr := []int{1, 3, 5, 7, 9}
    n := len(arr)
    ft := NewFenwickTree(n)
    for i := 1; i <= n; i++ {
        ft.Update(i, arr[i-1])
    }

    fmt.Println(ft.Query(3))       // 输出9
    fmt.Println(ft.RangeQuery(2, 4)) // 输出15
}
```

```c++
// 根据题目用 FenwickTree<int> t(n) 或者 FenwickTree<long long> t(n) 初始化
template<typename T>
class FenwickTree {
    vector<T> tree;

public:
    // 使用下标 1 到 n
    FenwickTree(int n) : tree(n + 1) {}

    // a[i] 增加 val
    // 1 <= i <= n
    // 时间复杂度 O(log n)
    void update(int i, T val) {
        for (; i < tree.size(); i += i & -i) {
            tree[i] += val;
        }
    }

    // 求前缀和 a[1] + ... + a[i]
    // 1 <= i <= n
    // 时间复杂度 O(log n)
    T pre(int i) const {
        T res = 0;
        for (; i > 0; i &= i - 1) {
            res += tree[i];
        }
        return res;
    }

    // 求区间和 a[l] + ... + a[r]
    // 1 <= l <= r <= n
    // 时间复杂度 O(log n)
    T query(int l, int r) const {
        if (r < l) {
            return 0;
        }
        return pre(r) - pre(l - 1);
    }
};
```

```java
class FenwickTree {
        private final int[] tree;
        private final int n;
        
        public  FenwickTree(int n) {
            this.n = n;
            this.tree = new int[n + 1];
        }
        
        private int lowbit(int x) {
            return x & -x;
        }
        
        public void update(int index, int value) {
            for (; index <= n; index += lowbit(index)) {
                tree[index] += value;
            }
        }
        
        public int query(int index) {
            int sum = 0;
            for (; index > 0; index -= lowbit(index)) {
                sum += tree[index];
            }
            return sum;
        }
        
        public int query(int left, int right) {
            return query(right) - query(left - 1);
        }
}
```

## **核心原理**

1. **二进制索引**  
   每个节点 `tree[i]` 管理原数组的一段区间，区间长度为 `lowbit(i)`（即 `i` 的二进制中最低位的 `1` 对应的值）。例如：
    - `lowbit(6) = 2`（`6` 的二进制为 `110`）。
    - `tree[6]` 管理原数组中 `a[5]` 和 `a[6]` 的和。

2. **操作逻辑**
    - **单点更新**：更新 `a[i]` 时，需更新所有覆盖 `i` 的 `tree` 节点。
    - **前缀和查询**：通过累加多个 `tree` 节点的值得到前 `i` 项的和。

## **关键操作**

| 操作        | 时间复杂度         | 说明                     |
|-----------|---------------|------------------------|
| **单点更新**  | $`O(\log n)`$ | 更新所有覆盖当前索引的 `tree` 节点。 |
| **前缀和查询** | $`O(\log n)`$ | 累加多个 `tree` 节点的值。      |
| **区间查询**  | $`O(\log n)`$ | 通过两次前缀和查询相减得到。         |

## **应用场景**

1. **动态前缀和**：实时统计前 `k` 个元素的和。
2. **逆序对计数**：结合离散化处理数组的逆序对问题。
3. **区间修改**：结合差分数组支持区间增减操作。

## **复杂度分析**

- **时间复杂度**：所有操作均为 $`O(\log n)`$。
- **空间复杂度**：$`O(n)`$。

通过树状数组，可以高效处理需要频繁更新和查询的场景，适用于算法竞赛和工程中的高性能需求。
