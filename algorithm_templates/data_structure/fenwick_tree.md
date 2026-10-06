# Fenwick Tree

A Fenwick tree efficiently supports **prefix sum queries** and **point updates**, each with a time complexity of $`O(\log n)`$.

The parent of node `t[x]` is `t[x+lowbit(x)]`.

Here, `lowbit` returns the lowest set bit in the binary representation (invert the bits, add 1, then apply `&` with the original value).

```python
class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)  # Indices start at 1

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int) -> None:
        """ Point update: a[idx] += delta """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        """ Query the prefix sum: a[1] + a[2] + ... + a[idx] """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

    def range_query(self, l: int, r: int) -> int:
        """ Range query: a[l] + a[l+1] + ... + a[r] """
        return self.query(r) - self.query(l - 1)


# Example
arr = [1, 3, 5, 7, 9]
n = len(arr)
ft = FenwickTree(n)
for i in range(1, n + 1):
    ft.update(i, arr[i - 1])

print(ft.query(3))  # Outputs 9 (1+3+5)
print(ft.range_query(2, 4))  # Outputs 15 (3+5+7)
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
        tree: make([]int, size+1), // Indices start at 1
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

    fmt.Println(ft.Query(3))       // Outputs 9
    fmt.Println(ft.RangeQuery(2, 4)) // Outputs 15
}
```

```c++
// Initialize with FenwickTree<int> t(n) or FenwickTree<long long> t(n), as required by the problem
template<typename T>
class FenwickTree {
    vector<T> tree;

public:
    // Use indices 1 through n
    FenwickTree(int n) : tree(n + 1) {}

    // Add val to a[i]
    // 1 <= i <= n
    // Time complexity: O(log n)
    void update(int i, T val) {
        for (; i < tree.size(); i += i & -i) {
            tree[i] += val;
        }
    }

    // Compute the prefix sum a[1] + ... + a[i]
    // 1 <= i <= n
    // Time complexity: O(log n)
    T pre(int i) const {
        T res = 0;
        for (; i > 0; i &= i - 1) {
            res += tree[i];
        }
        return res;
    }

    // Compute the range sum a[l] + ... + a[r]
    // 1 <= l <= r <= n
    // Time complexity: O(log n)
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

## **Core Principles**

1. **Binary indexing**  
   Each node `tree[i]` covers a range of the original array with length `lowbit(i)`, the value of the lowest set bit in the binary representation of `i`. For example:
    - `lowbit(6) = 2` (`6` is `110` in binary).
    - `tree[6]` stores the sum of `a[5]` and `a[6]` in the original array.

2. **How the operations work**
    - **Point update**: Updating `a[i]` requires updating every `tree` node that covers `i`.
    - **Prefix sum query**: Add the values of several `tree` nodes to obtain the sum of the first `i` elements.

## **Key Operations**

| Operation | Time Complexity | Description |
|-----------|---------------|------------------------|
| **Point update** | $`O(\log n)`$ | Update every `tree` node that covers the current index. |
| **Prefix sum query** | $`O(\log n)`$ | Add the values of several `tree` nodes. |
| **Range query** | $`O(\log n)`$ | Subtract the results of two prefix sum queries. |

## **Applications**

1. **Dynamic prefix sums**: Maintain the sum of the first `k` elements in real time.
2. **Counting inversions**: Combine with coordinate compression to count inversions in an array.
3. **Range updates**: Combine with a difference array to support range increments and decrements.

## **Complexity Analysis**

- **Time complexity**: All operations take $`O(\log n)`$.
- **Space complexity**: $`O(n)`$.

Fenwick trees efficiently handle frequent updates and queries, making them useful for competitive programming and engineering tasks that require high performance.

# Range Updates and Range Sums with Fenwick Trees and Difference Arrays

```c++
//
// Created by benhao on 2025/12/20.
//

#include <iostream>
#include <vector>

using namespace std;

class FenwickTree {
private:
    int n;
    vector<long long> bit1, bit2;  // Two Fenwick trees

    // General update operation
    void update(vector<long long>& bit, int idx, long long val) {
        while (idx <= n) {
            bit[idx] += val;
            idx += idx & -idx;  // Lowest set bit
        }
    }

    // General query operation
    long long query(const vector<long long>& bit, int idx) {
        long long sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx &= idx - 1;
        }
        return sum;
    }

public:
    FenwickTree(int size) : n(size) {
        bit1.resize(n + 1, 0);
        bit2.resize(n + 1, 0);
    }

    // Range update: add val to every element in [l, r]
    void range_update(int l, int r, long long val) {
        update(bit1, l, val);
        update(bit1, r + 1, -val);
        update(bit2, l, val * l);
        update(bit2, r + 1, -val * (r + 1));
    }

    // Point update: add val at index idx
    void point_update(int idx, long long val) {
        range_update(idx, idx, val);
    }

    // Compute the prefix sum over [1, k]
    long long prefix_sum(int k) {
        return (k + 1) * query(bit1, k) - query(bit2, k);
    }

    // Range query: compute the sum over [l, r]
    long long range_sum(int l, int r) {
        if (l > r) return 0;
        return prefix_sum(r) - prefix_sum(l - 1);
    }

    // Get the value in the original array
    long long get_value(int idx) {
        return range_sum(idx, idx);
    }
};

int main() {
    int n, q;
    std::cin >> n >> q;
    FenwickTree tree(n);
    for (int i = 0; i < n; i++) {
        int val;
        std::cin >> val;
        tree.point_update(i + 1, val);
    }
    for (int i = 0; i < q; i++) {
        int ty, l, r;
        std::cin >> ty;
        if (ty == 1) {
            int64_t v;
            std::cin >> l >> r >> v;
            tree.range_update(l, r, v);
        } else {
            std::cin >> l >> r;
            std::cout << tree.range_sum(l, r) << std::endl;
        }
    }
    return 0;
}
```

# Fenwick Tree Templates and Applications

```c++
//
// Created by benhao on 2026/1/9.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define lowbit(x) ((x)&(-(x)))

struct FenwickTree {
    vector<ll> arr;
    const size_t n;

    explicit FenwickTree(const size_t n): arr(n + 1), n(n) {}

    void add(size_t x, ll val);
    ll query(size_t x) const;
    ll query_range(size_t x, size_t y) const;
};

void FenwickTree::add(const size_t x, const ll val)  {
    for (size_t i = x; i <= n; i += lowbit(i)) {
        arr[i] += val;
    }
}

ll FenwickTree::query(const size_t x) const {
    ll res = 0;
    for (size_t i = x; i > 0; i -= lowbit(i)) {
        res += arr[i];
    }
    return res;
}

ll FenwickTree::query_range(const size_t x, const size_t y) const {
    return query(y) - query(x - 1);
}

int main() {
    int n, q;
    cin >> n >> q;
    FenwickTree f(n);
    int a;
    for (int i = 1; i <= n; ++i) {
        cin >> a;
        f.add(i, a);
    }
    int op, x, y;
    for (int i = 0; i < q; ++i) {
        cin >> op >> x >> y;
        if (op == 1) {
            f.add(x, y);
        } else {
            cout << f.query_range(x, y) << endl;
        }
    }
    return 0;
}
```
