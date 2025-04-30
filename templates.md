**算法模板**

# 目录

1. [数组](#数组)
    - [二分查找](#二分查找)
        - [带重复元素的旋转数组](#带重复元素的旋转数组)
    - [单调栈](#单调栈)
    - [滑动窗口](#滑动窗口)
    - [双指针](#双指针)
    - [排序](#排序)
    - [前缀和](#前缀和)
2. [堆](#堆)
    - [优先队列](#优先队列)
3. [字典树](#trie)
4. [深度优先搜索](#DFS)
5. [广度优先搜索](#BFS)
6. [拓扑排序](#拓扑排序)
7. [二进制](#二进制)
    - [位运算](#位运算)
    - [异或](#异或)
8. [动态规划](#动态规划)
    - [回文串切割](#回文串切割)
9. [并查集](#并查集)
10. [树状数组](#树状数组)
11. [线段树](#线段树)
12. [数学](#数学)
    - [费马平方和定理](#费马平方和定理)
13. [链表](#链表)
14. [二叉树](#二叉树)
15. [字符串](#字符串)
16. [回溯](#回溯)
    - [N皇后](#N皇后)
    - [排列组合](#排列组合)
        - [全排列](#全排列)
        - [重复元素全排列](#重复元素全排列)
        - [组合](#组合)
        - [重复元素组合](#重复元素组合)
        - [重复元素子集](#重复元素子集)
17. [其他](#其他)
    - [LRU缓存](#lru缓存)

---

# 数组

## 二分查找

**「二分」的本质是二段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。**

```python3
# bisect.bisect_left
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

```go
package main

func BinarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1
    for left <= right {
        mid := left + (right-left)/2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}
```

### 带重复元素的旋转数组

```go
// 这里的二段性是一段满足<target，另一段不满足
func binarySearch(nums []int, left, right, target int) int {
	l, r := left, right
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	if nums[r] == target {
		return r
	}
	return -1
}

func search(nums []int, target int) bool {
	n := len(nums)
	left, right := 0, n-1
	// 恢复二段性
	for left < right && nums[right] == nums[left] {
		right--
	}
	// 这里的二段性是一段满足>=nums[0]，另一段不满足
	for left < right {
		mid := left + (right-left+1)/2
		if nums[mid] >= nums[0] {
			left = mid
		} else {
			right = mid - 1
		}
	}
	idx := n
	if nums[right] >= nums[0] && right < n-1 {
		idx = right + 1
	}
	if target >= nums[0] {
		return binarySearch(nums, 0, idx-1, target) != -1
	} else {
		return binarySearch(nums, idx, n-1, target) != -1
	}
}
```

## 单调栈

```python3
def solve(nums):
    max_stack = []
    for i, num in enumerate(nums):
        while max_stack and num > nums[max_stack[-1]]:
            max_stack.pop()
        max_stack.append(i)
```

```go
package main

func subArrayRanges(nums []int) (ans int64) {
	n := len(nums)
	minStack, maxStack := make([]int, 0, n), make([]int, 0, n)
	for i := 0; i <= n; i++ {
		for len(maxStack) > 0 && (i == n || nums[i] > nums[maxStack[len(maxStack)-1]]) {
			j := maxStack[len(maxStack)-1]
			maxStack = maxStack[:len(maxStack)-1]
			left := -1
			if len(maxStack) > 0 {
				left = maxStack[len(maxStack)-1]
			}
			ans += int64(nums[j]) * int64(j-left) * int64(i-j)
		}
		maxStack = append(maxStack, i)
		for len(minStack) > 0 && (i == n || nums[i] < nums[minStack[len(minStack)-1]]) {
			j := minStack[len(minStack)-1]
			minStack = minStack[:len(minStack)-1]
			left := -1
			if len(minStack) > 0 {
				left = minStack[len(minStack)-1]
			}
			ans -= int64(nums[j]) * int64(j-left) * int64(i-j)
		}
		minStack = append(minStack, i)
	}
	return
}
```

## 滑动窗口

```python3
def max_sliding_window(nums, k):
    from collections import deque
    q = deque()
    res = []
    for i in range(len(nums)):
        if q and q[0] < i - k + 1:
            q.popleft()
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

```go
package main

def maxSlidingWindow(nums []int, k int) (ans []int) {
    q := make([]int, 0)
    for i := range nums {
        if len(q) > 0 && q[0] < i-k+1 {
            q = q[1:]
        }
        for len(q) > 0 && nums[q[len(q)-1]] < nums[i] {
            q = q[:len(q)-1]
        }
        q = append(q, i)
        if i >= k-1 {
            ans = append(ans, nums[q[0]])
        }
    }
    return
}
```

## 双指针

## 排序

## 前缀和

$`prefix\_sum[i] = \sum_{k=0}^{i-1} nums[k]`$

$`prefix\_sum[i] - prefix\_sum[j] = \sum_{k=j}^{i-1} nums[k]`$

```python
from itertools import accumulate


def pivotIndex(nums) -> int:
    pre_sum = [0] + list(accumulate(nums))
    for i, num in enumerate(nums):
        if pre_sum[i] == pre_sum[-1] - pre_sum[i + 1]:
            return i
    return -1
```

```go
package main

func pivotIndex(nums []int) int {
	n := len(nums)
	prefixSum := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefixSum[i+1] = prefixSum[i] + nums[i]
	}
	for i := 0; i < n; i++ {
		if prefixSum[i] == prefixSum[n]-prefixSum[i+1] {
			return i
		}
	}
	return -1
}
```

### 二维前缀和

$`prefix\_sum[i][j] = \sum_{k=0}^{i-1} \sum_{l=0}^{j-1} matrix[k][l]`$

$`prefix\_sum[i][j] - prefix\_sum[i][l] - prefix\_sum[k][j] + prefix\_sum[k][l] = \sum_{x=k}^{i-1} \sum_{y=l}^{j-1} matrix[x][y]`$

```python
def sum_region(matrix, row1, col1, row2, col2):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
    return pre_sum[row2 + 1][col2 + 1] - pre_sum[row1][col2 + 1] - pre_sum[row2 + 1][col1] + pre_sum[row1][col1]
```

```go
type NumMatrix struct {
    preSum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
    m := len(matrix)
    if m == 0 {
        return NumMatrix{}
    }
    n := len(matrix[0])
    preSum := make([][]int, m+1)
    for i := range preSum {
        preSum[i] = make([]int, n+1)
    }
    
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + matrix[i-1][j-1]
        }
    }
    return NumMatrix{preSum: preSum}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.preSum[row2+1][col2+1] - this.preSum[row1][col2+1] - this.preSum[row2+1][col1] + this.preSum[row1][col1]
}
```

---

# 堆

```python3
import heapq

arr = [3, 1, 4, 1, 5, 9]
heapq.heapify(arr)
heapq.heappush(arr, 2)
top_k = heapq.nlargest(3, arr)
top = heapq.heappop(arr)
```

```go
package main

import (
    "container/heap"
)

func kSmallest(nums []int, k int) (ans []int) {
	h := &IntHeap{}
	heap.Init(h)
    for _, num := range nums {
        heap.Push(h, num)
    }
	for i := 0; i < k; i++ {
        v := heap.Pop(h)
        ans = append(ans, v)
    }
	return
}

type IntHeap []int
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}
```

```go
package main

import (
    "container/heap"
    "math"
)

// 632 最小区间
func smallestRange(nums [][]int) []int {
	h := make(hp, len(nums))
	r := math.MinInt
	for i, arr := range nums {
		h[i] = tuple{arr[0], i, 0} // 把每个列表的第一个元素入堆
		r = max(r, arr[0])
	}
	heap.Init(&h)

	ansL, ansR := h[0].x, r            // 第一个合法区间的左右端点
	for h[0].j+1 < len(nums[h[0].i]) { // 堆顶列表有下一个元素
		x := nums[h[0].i][h[0].j+1] // 堆顶列表的下一个元素
		r = max(r, x)               // 更新合法区间的右端点
		h[0].x = x                  // 替换堆顶
		h[0].j++
		heap.Fix(&h, 0)
		l := h[0].x // 当前合法区间的左端点
		if r-l < ansR-ansL {
			ansL, ansR = l, r
		}
	}
	return []int{ansL, ansR}
}

type tuple struct{ x, i, j int }
type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].x < h[j].x }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (hp) Push(any)             {} // 没用到，可以不写
func (hp) Pop() (_ any)         { return }
```

## 优先队列

```go
// This example demonstrates a priority queue built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
)

// An Item is something we manage in a priority queue.
type Item struct {
	value    string // The value of the item; arbitrary.
	priority int    // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // don't stop the GC from reclaiming the item eventually
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value string, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

// This example creates a PriorityQueue with some items, adds and manipulates an item,
// and then removes the items in priority order.
func main() {
	// Some items and their priorities.
	items := map[string]int{
		"banana": 3, "apple": 2, "pear": 4,
	}

	// Create a priority queue, put the items in it, and
	// establish the priority queue (heap) invariants.
	pq := make(PriorityQueue, len(items))
	i := 0
	for value, priority := range items {
		pq[i] = &Item{
			value:    value,
			priority: priority,
			index:    i,
		}
		i++
	}
	heap.Init(&pq)

	// Insert a new item and then modify its priority.
	item := &Item{
		value:    "orange",
		priority: 1,
	}
	heap.Push(&pq, item)
	pq.update(item, item.value, 5)

	// Take the items out; they arrive in decreasing priority order.
	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		fmt.Printf("%.2d:%s ", item.priority, item.value)
	}
}
```

---

# Trie

```python3
root = {}


def insert(word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True


def search(word):
    node = root
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '#' in node


def starts_with(prefix):
    node = root
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True
```

```go
package main

type TrieNode struct {
    children map[rune]*TrieNode
    isEnd    bool
}

func TrieNodeConstructor() *TrieNode {
    return &TrieNode{children: make(map[rune]*TrieNode)}
}

func (t *TrieNode) Insert(word string) {
    node := t
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            node.children[char] = TrieNodeConstructor()
        }
        node = node.children[char]
    }
    node.isEnd = true
}

func (t *TrieNode) Search(word string) bool {
    node := t
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return node.isEnd
}

func (t *TrieNode) StartsWith(prefix string) bool {
    node := t
    for _, char := range prefix {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return true
}
```

---

# DFS

---

# BFS

---

# 拓扑排序

---

# 二进制

## 位运算

## 异或

`xor`运算的性质：
1. $`a \oplus a = 0`$
2. $`a \oplus 0 = a`$
3. $`a \oplus b \oplus c = a \oplus c \oplus b`$

```python3
def single_number(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans
```

```go
package main

func singleNumber(nums []int) int {
    ans := 0
    for _, num := range nums {
        ans ^= num
    }
    return ans
}
```

---

# 动态规划

## 回文串切割

```python
def min_cut(s):
    """
    :type s: str
    :rtype: int
    """

    n = len(s)

    is_palindrome = [[True for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            is_palindrome[j][i] = s[j] == s[i] and is_palindrome[j + 1][i - 1]

    dp = [i for i in range(n)]
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(1, i + 1):
                if is_palindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[-1]

```

```go
package main

func minCut(s string) int {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := 0; i < n; i++ {
		isPalindrome[i] = make([]bool, n)
	}
	for i := 0; i < n; i++ {
		for j := i; j >= 0; j-- {
			if s[j] == s[i] && (i-j <= 1 || isPalindrome[j+1][i-1]) {
				isPalindrome[j][i] = true
			}
		}
	}
	dp := make([]int, n)
	for i := 1; i < n; i++ {
		dp[i] = i
		if isPalindrome[0][i] {
			dp[i] = 0
		} else {
			for j := 1; j <= i; j++ {
				if isPalindrome[j][i] {
					dp[i] = min(dp[i], dp[j-1]+1)
				}
			}
		}
	}
	return dp[n-1]
}
```

---

# 并查集

并查集（Union-Find）是一种数据结构，用于处理一些不交集的合并及查询问题。它支持两种操作：
1. **Find**：查找元素所在的集合。
2. **Union**：合并两个集合。

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # 已经在同一集合

        # 按秩合并
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
```

```go
package main

type UnionFind struct {
    parent []int
    rank   []int
}

func NewUnionFind(size int) *UnionFind {
    uf := &UnionFind{
        parent: make([]int, size),
        rank:   make([]int, size),
    }
    for i := range uf.parent {
        uf.parent[i] = i
        uf.rank[i] = 1
    }
    return uf
}

func (uf *UnionFind) Find(x int) int {
    for uf.parent[x] != x {
        uf.parent[x] = uf.parent[uf.parent[x]] // 路径压缩
        x = uf.parent[x]
    }
    return x
}

func (uf *UnionFind) Union(x, y int) bool {
    rootX := uf.Find(x)
    rootY := uf.Find(y)
    
    if rootX == rootY {
        return false // 已经在同一集合
    }
    
    // 按秩合并
    if uf.rank[rootX] > uf.rank[rootY] {
        uf.parent[rootY] = rootX
    } else {
        uf.parent[rootX] = rootY
        if uf.rank[rootX] == uf.rank[rootY] {
            uf.rank[rootY]++
        }
    }
    return true
}

func (uf *UnionFind) IsConnected(x, y int) bool {
    return uf.Find(x) == uf.Find(y)
}
```

---

# 树状数组

---

# 线段树

线段树是一种二叉树数据结构，用于高效解决**区间查询**（如区间求和、最大值、最小值）和**单点/区间更新**问题。时间复杂度为 O(log n)。

- 核心思想
    - 结构：每个节点代表一个区间，叶子节点代表单个元素，内部节点合并子区间的信息。
    - 分治：将区间不断二分，直到不可分割。
    - 合并：父节点存储子节点信息的聚合值（如求和、最大值等）。

- 线段树操作
    - 构建：递归分割区间，计算初始值。
    - 查询：分解目标区间，合并覆盖区间的结果。
    - 更新：更新叶子节点，回溯更新父节点。

| 类型 | 空间复杂度 | 使用场景
| -- | -- | -- |
| 常规线段树 | O(4n) | 区间较小（如 n ≤ 1e6）
| 动态开点线段树 | O(Q log R) | 区间极大（如 R = 1e18）

## 常规线段树

```python
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)  # 预分配4倍空间
        self.build(0, 0, self.n - 1, data)
    
    def build(self, node, start, end, data):
        """ 递归构建线段树 """
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self.build(left_node, start, mid, data)
            self.build(right_node, mid + 1, end, data)
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
st.update(2, 10)             # 更新索引2为10
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
        self.end = end      # 区间右端点
    
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
        return self._query(node.left, l, mid, ql, qr) + \
               self._query(node.right, mid + 1, r, ql, qr)
    
    def query_range(self, l, r):
        """查询区间 [l, r] 的和"""
        return self._query(self.root, self.start, self.end, l, r)

# 使用示例（假设区间范围为 [0, 1e9]）
dst = DynamicSegmentTree(0, 10**9)
dst.update_range(1, 3, 5)      # 区间 [1,3] 增加5
print(dst.query_range(2, 4))   # 输出 5（仅覆盖到3）
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
        self.left = None    # 动态指针：左子节点
        self.right = None   # 动态指针：右子节点
        self.val = 0        # 当前区间的聚合值（根据场景修改初始值）
        self.lazy = 0       # 惰性标记（根据场景定义含义）

class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end      # 区间右端点

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
        return self._query(node.left, l, mid, ql, qr) + \
               self._query(node.right, mid + 1, r, ql, qr)

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
| 技巧                | 适用场景                        | 实现方式                                                                 |
|---------------------|-------------------------------|------------------------------------------------------------------------|
| **节点池复用**       | 高频更新/查询操作               | 预分配节点对象池，通过索引管理而非动态创建/销毁                                 |
| **迭代实现**         | 避免递归栈溢出                  | 用栈或队列模拟递归过程                                                   |
| **离散化坐标**       | 区间端点稀疏但数量有限           | 将原始坐标映射到紧凑的整数范围，减少动态开点需求                               |


## 不同场景下的线段树修改指南
线段树的核心逻辑在不同场景下需要调整的部分主要集中在 **聚合方式** 和 **惰性标记处理** 上。以下是关键修改点：

| 场景              | 修改点                                                                                     | 示例（区间求和 → 区间最大值）                     |
|-------------------|------------------------------------------------------------------------------------------|------------------------------------------------|
| **聚合逻辑**       | 合并子区间结果的方式（如 `sum` → `max`）                                                    | `node.val = max(left.val, right.val)`          |
| **惰性标记处理**   | 区间更新时的标记传递逻辑（如加减 → 赋值）                                                    | `lazy` 存储待赋值的值而非增量                     |
| **初始化值**       | 根据聚合逻辑选择初始值（如求和初始化为0，最大值初始化为负无穷）                                  | `self.val = -inf`                              |
| **区间合并方式**   | 查询时如何合并部分覆盖区间的结果（如求和直接相加，最大值取子区间最大值）                          | `return max(left_query, right_query)`          |


## 场景适配示例

- 示例 1：区间最大值 + 区间更新
```python
class Node:
    __slots__ = ["left", "right", "val", "lazy"]  # 优化内存

    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end  # 区间右端点
    
    def _push_up(self, node):
        node.val = max(node.left.val, node.right.val)

    def _push_down(self, node, l, r):
        # 动态创建子节点并下推惰性标记
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:
            # 更新左子节点
            node.left.val += node.lazy
            node.left.lazy += node.lazy
            # 更新右子节点
            node.right.val += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:  # 完全覆盖
            node.val += val
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        self._push_up(node)

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
        return max(self._query(node.left, l, mid, ql, qr), self._query(
            node.right, mid + 1, r, ql, qr
        ))

    def query_range(self, l, r):
        """查询区间 [l, r] 的和"""
        return self._query(self.root, self.start, self.end, l, r)
```


- 示例 1：区间最大值 + 区间赋值
```python
# 修改点 1：节点初始化
class Node:
    def __init__(self):
        self.val = -float('inf')  # 初始化为负无穷
        self.lazy = None          # 赋值操作使用 None 表示无标记

# 修改点 2：push_down 逻辑
def _push_down(self, node, l, r):
    if node.left is None:
        node.left = Node()
    if node.right is None:
        node.right = Node()
    if node.lazy is not None:
        node.left.val = node.lazy  # 直接赋值
        node.left.lazy = node.lazy
        node.right.val = node.lazy
        node.right.lazy = node.lazy
        node.lazy = None

# 修改点 3：update 逻辑
def _update(self, node, l, r, ul, ur, val):
    if ul <= l and r <= ur:
        node.val = val            # 直接赋值
        node.lazy = val
        return
    # ... 其他部分不变
```

- 示例 2：区间乘法更新
```python
# 修改点：lazy 标记处理
def _push_down(self, node, l, r):
    if node.left is None:
        node.left = Node()
    if node.right is None:
        node.right = Node()
    if node.lazy != 1:  # 乘法初始标记为1
        node.left.val *= node.lazy
        node.left.lazy *= node.lazy
        node.right.val *= node.lazy
        node.right.lazy *= node.lazy
        node.lazy = 1
```

---

# 数学

## 费马平方和定理

- **定理内容**

一个奇素数$`p`$, 可以表示为两个整数的平方和（即$`p = x^2 + y^2`$），当且仅当$$p \equiv 1 \pmod{4}$$

- **证明思路（简述）**

如果$`p \equiv 1 \pmod{4}`$，可以通过数论方法证明$`p`$可以表示为两个平方数之和。
如果$`p \equiv 3 \pmod{4}`$，则$`p`$无法表示为两个平方数之和。

- **示例**

$`5 = 2^2 + 1^2`$，且$`5 \equiv 1 \pmod{4}`$

$`13 = 3^2 + 2^2`$，且$`13 \equiv 1 \pmod{4}`$

$`7`$无法表示为两个平方数之和，因为$`7 \equiv 3 \pmod{4}`$

---

# 链表

---

# 二叉树

---

# 字符串

---

# 回溯

## N皇后

```python3
def total_n_queens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    # queens[i] means the column position for queen at i-1 th row
    # lu_rd: left up corner to right down corner
    # ld_ru: left down corner to right up corner
    def dfs(queens, lu_rd, ld_ru):
        row = len(queens)
        if row == n:
            nonlocal ans
            ans += 1
            return
        for col in range(n):
            if col not in queens and col - row not in lu_rd and row + col not in ld_ru:
                queens.add(col)
                lu_rd.add(col - row)
                ld_ru.add(row + col)
                dfs(queens, lu_rd, ld_ru)
                queens.remove(col)
                lu_rd.remove(col - row)
                ld_ru.remove(row + col)

    ans = 0
    dfs(set(), set(), set())
    return ans
```

```go
package main

func totalNQueens(n int) (ans int) {
	cols := map[int]interface{}{}
	rowCols := map[int]interface{}{}
	colRows := map[int]interface{}{}

	var backtrack func()
	backtrack = func() {
		r := len(cols)
		if r == n {
			ans++
			return
		}
		for c := 0; c < n; c++ {
			if _, ok := cols[c]; ok {
				continue
			}
			rc := r + c
			if _, ok := rowCols[rc]; ok {
				continue
			}
			cr := r - c
			if _, ok := colRows[cr]; ok {
				continue
			}
			cols[c] = nil
			rowCols[rc] = nil
			colRows[cr] = nil
			backtrack()
			delete(cols, c)
			delete(rowCols, rc)
			delete(colRows, cr)
		}
	}
	backtrack()
	return
}
```

## 排列组合

### 全排列

```python3
def permute(nums):
    ans = []

    def dfs(x):
        if x == len(nums) - 1:
            ans.append(list(nums))
            return
        for i in range(x, len(nums)):
            nums[i], nums[x] = nums[x], nums[i]
            dfs(x + 1)
            nums[i], nums[x] = nums[x], nums[i]

    dfs(0)
    return ans
```

```go
package main

func permute(nums []int) (ans [][]int) {
	var backtrack func(int)
	backtrack = func(idx int) {
		if idx == len(nums) {
			tmp := make([]int, len(nums))
			copy(tmp, nums)
			ans = append(ans, tmp)
			return
		}
		for i := idx; i < len(nums); i++ {
			nums[i], nums[idx] = nums[idx], nums[i]
			backtrack(idx + 1)
			nums[i], nums[idx] = nums[idx], nums[i]
		}
	}
	backtrack(0)
	return
}
```

#### 重复元素全排列

```python3
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    if i < 0:
        return
    j = i + 1
    while j < n and arr[j] <= arr[i]:
        j += 1
    arr[i], arr[j] = arr[j], arr[i]
```

```go
package main

func NextPermutation(nums []int) {
	n := len(nums)
	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}
	for l, r := i+1, n-1; l < r; l, r = l+1, r-1 {
		nums[l], nums[r] = nums[r], nums[l]
	}
	if i < 0 {
		return
	}
	j := i + 1
	for j < n && nums[j] <= nums[i] {
		j++
	}
	nums[i], nums[j] = nums[j], nums[i]
}
```

### 组合

```python3
def combinationSum(candidates, target: int):
    candidates.sort()
    ans = []
    path = []

    def dfs(x, s):
        if s == 0:
            ans.append(list(path))
            return
        if x < 0 or s < 0:
            return
        # 不选当前
        dfs(x - 1, s)
        # 选当前
        path.append(candidates[x])
        dfs(x, s - candidates[x])
        path.pop()

    dfs(len(candidates) - 1, target)
    return ans
```

```go
func combinationSum(candidates []int, target int) (ans [][]int) {
	var dfs func([]int, int, int)
	dfs = func(path []int, idx int, s int) {
		if s == 0 {
			ans = append(ans, append([]int(nil), path...))
			return
		}
		if idx == len(candidates) {
			return
		}
		if candidates[idx] <= s {
			path = append(path, candidates[idx])
			dfs(path, idx, s-candidates[idx])
			path = path[:len(path)-1]
		}
		dfs(path, idx+1, s)
	}

	dfs([]int{}, 0, target)
	return
}
```

#### 重复元素组合

```python3
def combinationSum2(candidates, target: int):
    ans = []
    path = []
    candidates.sort()
    n = len(candidates)

    def backtrack(idx, remain):
        if remain < 0:
            return
        if not remain:
            ans.append(list(path))
            return
        if idx == n:
            return
        path.append(candidates[idx])
        backtrack(idx + 1, remain - candidates[idx])
        path.pop()
        nxt = idx + 1
        while nxt < n and candidates[nxt] == candidates[nxt - 1]:
            nxt += 1
        backtrack(nxt, remain)

    backtrack(0, target)
    return ans
```

```go
func combinationSum2(candidates []int, target int) (ans [][]int) {
	sort.Ints(candidates)
	n := len(candidates)
	var backtrack func(idx int, remain int, path []int)
	backtrack = func(idx, remain int, path []int) {
		if remain < 0 {
			return
		}
		if remain == 0 {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		if idx == n {
			return
		}
		path = append(path, candidates[idx])
		backtrack(idx+1, remain-candidates[idx], path)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && candidates[nxt] == candidates[nxt-1] {
			nxt++
		}
		backtrack(nxt, remain, path)
	}
	backtrack(0, target, make([]int, 0))
	return
}
```

#### 重复元素子集

```go
func subsetsWithDup(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	path := []int{}

	var backtrack func(idx int)
	backtrack = func(idx int) {
		if idx == n {
			cp := make([]int, len(path))
			copy(cp, path)
			ans = append(ans, cp)
			return
		}
		path = append(path, nums[idx])
		backtrack(idx + 1)
		path = path[:len(path)-1]
		nxt := idx + 1
		for nxt < n && nums[nxt] == nums[idx] {
			nxt++
		}
		backtrack(nxt)
	}
	backtrack(0)
	return
}
```

---

# 其他

## lru缓存

----