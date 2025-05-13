# **算法模板**

# 目录

- [数组](#数组)
    - [二分查找](#二分查找)
        - [带重复元素的旋转数组](#带重复元素的旋转数组)
    - [单调栈](#单调栈)
    - [滑动窗口](#滑动窗口)
    - [双指针](#双指针)
    - [排序](#排序)
    - [前缀和](#前缀和)
- [数据结构](#数据结构)
    - [堆](#堆)
        - [优先队列](#优先队列)
    - [链表](#链表)
        - [反转链表](#反转链表)
        - [快慢指针](#快慢指针)
    - [二叉树](#二叉树)
        - [前序遍历](#前序遍历)
        - [中序遍历](#中序遍历)
        - [后序遍历](#后序遍历)
        - [AVL树](#AVL树)
        - [红黑树](#红黑树)
    - [字典树](#trie)
    - [并查集](#并查集)
    - [树状数组](#树状数组)
    - [线段树](#线段树)
        - [常规线段树](#常规线段树)
        - [动态开点](#动态开点)
        - [动态指针](#动态指针)
            - [动态指针管理注意事项](#动态指针管理注意事项)
            - [性能优化技巧](#性能优化技巧)
        - [动态开点线段树应用](#动态开点线段树应用)
            - [区间求和](#区间求和)
            - [区间最小值](#区间最小值)
            - [区间最大值](#区间最大值)
            - [区间更新](#区间更新)
    - [跳表](#跳表)
- [图论](#图论)
    - [存图方式](#存图方式)
    - [深度优先搜索](#DFS)
    - [广度优先搜索](#BFS)
    - [最短路径](#最短路径)
        - [dijkstra](#dijkstra算法优先队列实现)
    - [拓扑排序](#拓扑排序)
- [二进制](#二进制)
    - [位运算](#位运算)
    - [异或](#异或)
- [动态规划](#动态规划)
    - [回文串切割](#回文串切割)
    - [数位DP](#数位dp)
- [数学](#数学)
    - [费马平方和定理](#费马平方和定理)
- [字符串](#字符串)
    - [KMP算法](#kmp算法模板)
- [回溯](#回溯)
    - [N皇后](#N皇后)
    - [排列组合](#排列组合)
        - [全排列](#全排列)
        - [重复元素全排列](#重复元素全排列)
        - [组合](#组合)
        - [重复元素组合](#重复元素组合)
        - [重复元素子集](#重复元素子集)
- [其他](#其他)
    - [LRU缓存](#lru缓存)
    - [倍增](#倍增)

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
package main

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

### 单调栈适用场景
单调栈可以在时间复杂度为$`O(n)`$，求解出某个元素左边或者右边第一个比它大或者小的元素。

单调栈一般用于解决一下几种问题：

- 寻找左侧第一个比当前元素大的元素。
- 寻找左侧第一个比当前元素小的元素。
- 寻找右侧第一个比当前元素大的元素。
- 寻找右侧第一个比当前元素小的元素。

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

func maxSlidingWindow(nums []int, k int) (ans []int) {
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

- 双指针技巧通常用于处理数组或链表问题，如**快慢指针**检测循环、**左右指针**解决有序数组问题等。

### 示例：移除元素（原地删除）
```python
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

```go
package main

func removeElement(nums []int, val int) int {
    slow := 0
    for fast := 0; fast < len(nums); fast++ {
        if nums[fast] != val {
            nums[slow] = nums[fast]
            slow++
        }
    }
    return slow
}
```

### 示例：有序数组两数之和
```python
def two_sum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left+1, right+1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

```go
package main

func twoSum(nums []int, target int) []int {
    left, right := 0, len(nums)-1
    for left < right {
        sum := nums[left] + nums[right]
        if sum == target {
            return []int{left+1, right+1}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}
```

## 排序

### 快速排序（Python）
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### 归并排序（Go）
```go
package main

func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr)/2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    result := make([]int, 0)
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] < right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }
    result = append(result, left[i:]...)
    result = append(result, right[j:]...)
    return result
}
```

## 前缀和

$`prefix\_sum[i] = \sum_{k=0}^{i-1} nums[k]`$

$`prefix\_sum[i] - prefix\_sum[j] = \sum_{k=j}^{i-1} nums[k]`$

```python
from itertools import accumulate


def pivot_index(nums) -> int:
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
package main

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

# 数据结构

## 堆

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
        v := heap.Pop(h).(int)
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
	heap.Init(h)

	ansL, ansR := h[0].x, r            // 第一个合法区间的左右端点
	for h[0].j+1 < len(nums[h[0].i]) { // 堆顶列表有下一个元素
		x := nums[h[0].i][h[0].j+1] // 堆顶列表的下一个元素
		r = max(r, x)               // 更新合法区间的右端点
		h[0].x = x                  // 替换堆顶
		h[0].j++
		heap.Fix(h, 0)
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

## 链表

### 反转链表
```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

```go
package main

type ListNode struct {
    Val  int
    Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    curr := head
    for curr != nil {
        next := curr.Next
        curr.Next = prev
        prev = curr
        curr = next
    }
    return prev
}
```

### 快慢指针

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def half_head(head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
```
```go
package main

type ListNode struct {
    Val  int
    Next *ListNode
}

func halfHead(head *ListNode) *ListNode {
	fast, slow := head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	return slow
}
```

---

## 二叉树


### 前序遍历
```python
def preorder(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res
```

```go
package main

type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
    res := []int{}
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        res = append(res, node.Val)
        dfs(node.Left)
        dfs(node.Right)
    }
    dfs(root)
    return res
}
```

### 中序遍历

### 后序遍历

### AVL树

### 红黑树

- **红黑树**是一种自平衡的二叉搜索树，通过颜色标记和旋转操作保持平衡，确保插入、删除和查找的时间复杂度为 **O(log n)**。
- 核心性质
    1. **颜色规则**：每个节点是红色或黑色。
    2. **根节点**：根必须是黑色。
    3. **叶子节点**：所有叶子（NIL节点）是黑色。
    4. **红色节点限制**：红色节点的子节点必须是黑色（无连续红节点）。
    5. **黑高一致**：从任意节点到其所有叶子节点的路径中，黑色节点数量相同。
- [855. 考场就座](./problems/problems_855/solution.go)


```python
class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')  # 哨兵叶子节点
        self.root = self.NIL

    def left_rotate(self, x):
        """ 左旋操作（维护红黑树平衡） """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """ 右旋操作（镜像对称） """
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        """ 插入后修复颜色和结构 """
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # 叔节点
                if y.color == 'RED':       # Case 1: 叔节点为红
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:  # Case 2: 三角结构转直线
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3: 调整颜色并旋转
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # 镜像处理父节点在右侧的情况
                # TODO: 类似左侧逻辑 ...
                pass
            if z == self.root:
                break
        self.root.color = 'BLACK'

    def insert(self, key):
        """ 插入节点并修复 """
        z = Node(key)
        z.parent = self.NIL
        z.left = self.NIL
        z.right = self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:  # 标准BST插入
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.color = 'RED'
        self.insert_fixup(z)

# 使用示例
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(5)
```

```go
package main

type Node struct {
	key    int
	color  bool // true: red, false: black
	left   *Node
	right  *Node
	parent *Node
}

const (
	RED   = true
	BLACK = false
)

type RedBlackTree struct {
	root *Node
	nil  *Node // Sentinel node
}

func NewRedBlackTree() *RedBlackTree {
	nilNode := &Node{color: BLACK}
	return &RedBlackTree{
		root: nilNode,
		nil:  nilNode,
	}
}

func (t *RedBlackTree) leftRotate(x *Node) {
	y := x.right
	x.right = y.left
	if y.left != t.nil {
		y.left.parent = x
	}
	y.parent = x.parent
	if x.parent == t.nil {
		t.root = y
	} else if x == x.parent.left {
		x.parent.left = y
	} else {
		x.parent.right = y
	}
	y.left = x
	x.parent = y
}

func (t *RedBlackTree) rightRotate(y *Node) {
	x := y.left
	y.left = x.right
	if x.right != t.nil {
		x.right.parent = y
	}
	x.parent = y.parent
	if y.parent == t.nil {
		t.root = x
	} else if y == y.parent.right {
		y.parent.right = x
	} else {
		y.parent.left = x
	}
	x.right = y
	y.parent = x
}

func (t *RedBlackTree) insertFixup(z *Node) {
	for z.parent.color == RED {
		if z.parent == z.parent.parent.left {
			y := z.parent.parent.right
			if y.color == RED {
				z.parent.color = BLACK
				y.color = BLACK
				z.parent.parent.color = RED
				z = z.parent.parent
			} else {
				if z == z.parent.right {
					z = z.parent
					t.leftRotate(z)
				}
				z.parent.color = BLACK
				z.parent.parent.color = RED
				t.rightRotate(z.parent.parent)
			}
		} else {
			y := z.parent.parent.left
			if y.color == RED {
				z.parent.color = BLACK
				y.color = BLACK
				z.parent.parent.color = RED
				z = z.parent.parent
			} else {
				if z == z.parent.left {
					z = z.parent
					t.rightRotate(z)
				}
				z.parent.color = BLACK
				z.parent.parent.color = RED
				t.leftRotate(z.parent.parent)
			}
		}
	}
	t.root.color = BLACK
}

func (t *RedBlackTree) Insert(key int) {
	z := &Node{
		key:    key,
		color:  RED,
		left:   t.nil,
		right:  t.nil,
		parent: t.nil,
	}
	y := t.nil
	x := t.root
	for x != t.nil {
		y = x
		if z.key < x.key {
			x = x.left
		} else {
			x = x.right
		}
	}
	z.parent = y
	if y == t.nil {
		t.root = z
	} else if z.key < y.key {
		y.left = z
	} else {
		y.right = z
	}
	t.insertFixup(z)
}

func (t *RedBlackTree) transplant(u, v *Node) {
	if u.parent == t.nil {
		t.root = v
	} else if u == u.parent.left {
		u.parent.left = v
	} else {
		u.parent.right = v
	}
	v.parent = u.parent
}

func (t *RedBlackTree) deleteFixup(x *Node) {
	for x != t.root && x.color == BLACK {
		if x == x.parent.left {
			w := x.parent.right
			if w.color == RED {
				w.color = BLACK
				x.parent.color = RED
				t.leftRotate(x.parent)
				w = x.parent.right
			}
			if w.left.color == BLACK && w.right.color == BLACK {
				w.color = RED
				x = x.parent
			} else {
				if w.right.color == BLACK {
					w.left.color = BLACK
					w.color = RED
					t.rightRotate(w)
					w = x.parent.right
				}
				w.color = x.parent.color
				x.parent.color = BLACK
				w.right.color = BLACK
				t.leftRotate(x.parent)
				x = t.root
			}
		} else {
			w := x.parent.left
			if w.color == RED {
				w.color = BLACK
				x.parent.color = RED
				t.rightRotate(x.parent)
				w = x.parent.left
			}
			if w.right.color == BLACK && w.left.color == BLACK {
				w.color = RED
				x = x.parent
			} else {
				if w.left.color == BLACK {
					w.right.color = BLACK
					w.color = RED
					t.leftRotate(w)
					w = x.parent.left
				}
				w.color = x.parent.color
				x.parent.color = BLACK
				w.left.color = BLACK
				t.rightRotate(x.parent)
				x = t.root
			}
		}
	}
	x.color = BLACK
}

func (t *RedBlackTree) Delete(key int) {
	z := t.root
	for z != t.nil && z.key != key {
		if key < z.key {
			z = z.left
		} else {
			z = z.right
		}
	}
	if z == t.nil {
		return
	}

	y := z
	yOriginalColor := y.color
	var x *Node
	if z.left == t.nil {
		x = z.right
		t.transplant(z, z.right)
	} else if z.right == t.nil {
		x = z.left
		t.transplant(z, z.left)
	} else {
		y = t.minimum(z.right)
		yOriginalColor = y.color
		x = y.right
		if y.parent == z {
			x.parent = y
		} else {
			t.transplant(y, y.right)
			y.right = z.right
			y.right.parent = y
		}
		t.transplant(z, y)
		y.left = z.left
		y.left.parent = y
		y.color = z.color
	}
	if yOriginalColor == BLACK {
		t.deleteFixup(x)
	}
}

func (t *RedBlackTree) minimum(x *Node) *Node {
	for x.left != t.nil {
		x = x.left
	}
	return x
}

func (t *RedBlackTree) InOrder() []int {
	var result []int
	t.inOrderHelper(t.root, &result)
	return result
}

func (t *RedBlackTree) inOrderHelper(node *Node, result *[]int) {
	if node != t.nil {
		t.inOrderHelper(node.left, result)
		*result = append(*result, node.key)
		t.inOrderHelper(node.right, result)
	}
}
```

#### 关键操作解析
| 操作       | 说明                                         |
|----------|--------------------------------------------|
| **左旋**   | 将右子节点提升为父节点，原父节点变为左子节点，保持二叉搜索树性质。          |
| **右旋**   | 将左子节点提升为父节点，原父节点变为右子节点，镜像对称操作。             |
| **插入修复** | 通过颜色翻转和旋转解决连续红节点问题，分三种情况处理（叔节点颜色决定策略）。     |
| **删除修复** | 处理双重黑节点问题，通过兄弟节点颜色和子节点分布调整（代码较复杂，未展示完整逻辑）。 |

#### 应用场景
1. **有序映射/集合**：如Java的`TreeMap`、C++的`std::map`。
2. **数据库索引**：B+树的变种常用于数据库索引，红黑树用于内存数据管理。
3. **任务调度**：Linux内核的公平调度器（CFS）用红黑树管理进程队列。

通过实现红黑树，可以深入理解自平衡数据结构的设计思想，但实际开发中建议直接使用语言标准库中的有序容器（如Python的`sortedcontainers`或Golang的第三方库）。

---

## Trie

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

## 并查集

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


## 树状数组

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
        return self.query(r) - self.query(l-1)

# 示例
arr = [1, 3, 5, 7, 9]
n = len(arr)
ft = FenwickTree(n)
for i in range(1, n+1):
    ft.update(i, arr[i-1])

print(ft.query(3))      # 输出9 (1+3+5)
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


### **核心原理**
1. **二进制索引**  
   每个节点 `tree[i]` 管理原数组的一段区间，区间长度为 `lowbit(i)`（即 `i` 的二进制中最低位的 `1` 对应的值）。例如：
   - `lowbit(6) = 2`（`6` 的二进制为 `110`）。
   - `tree[6]` 管理原数组中 `a[5]` 和 `a[6]` 的和。

2. **操作逻辑**  
   - **单点更新**：更新 `a[i]` 时，需更新所有覆盖 `i` 的 `tree` 节点。
   - **前缀和查询**：通过累加多个 `tree` 节点的值得到前 `i` 项的和。

### **关键操作**
| 操作        | 时间复杂度         | 说明                     |
|-----------|---------------|------------------------|
| **单点更新**  | $`O(\log n)`$ | 更新所有覆盖当前索引的 `tree` 节点。 |
| **前缀和查询** | $`O(\log n)`$ | 累加多个 `tree` 节点的值。      |
| **区间查询**  | $`O(\log n)`$ | 通过两次前缀和查询相减得到。         |

### **应用场景**
1. **动态前缀和**：实时统计前 `k` 个元素的和。
2. **逆序对计数**：结合离散化处理数组的逆序对问题。
3. **区间修改**：结合差分数组支持区间增减操作。

### **复杂度分析**
- **时间复杂度**：所有操作均为 $`O(\log n)`$。
- **空间复杂度**：$`O(n)`$。

通过树状数组，可以高效处理需要频繁更新和查询的场景，适用于算法竞赛和工程中的高性能需求。

---

## 线段树

线段树是一种二叉树数据结构，用于高效解决**区间查询**（如区间求和、最大值、最小值）和**单点/区间更新**问题。时间复杂度为 O(log n)。

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

### 常规线段树

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

### 动态开点

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

### 动态指针

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


#### 动态指针管理注意事项
1. **内存控制**：
   - 在 Python 中，未被引用的节点会被自动回收；在 Go 中需手动管理（或依赖 GC）。
   - 在极端情况下，可添加节点复用池减少内存分配开销。
2. **递归深度**：
   - 处理极大区间时可能触发栈溢出，可改用迭代实现或调整递归深度限制。
3. **标记下推顺序**：
   - 必须在访问子节点前调用 `push_down`，确保子节点已创建且标记已处理。


#### 性能优化技巧
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
            self.val = 0       # 区间和
            self.lazy = 0      # 延迟增加量
    
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
        return self._query(node.left, l, mid, ql, qr) + \
               self._query(node.right, mid + 1, r, ql, qr)
    
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
            self.val = float('inf')     # 初始为无穷大
            self.lazy = None            # 延迟赋值标记
    
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
            node.val = val     # 直接赋值
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
            self.lazy = 0                # 延迟增加量
    
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
            node.max_val += val     # 增加最大值
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
            self.val = 0        # 当前区间的值（全部相同）
            self.lazy = None    # 延迟赋值标记
    
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

---

## 跳表

[Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)

```python
import random
from typing import Optional

class SkipNode:
    def __init__(self, val: int = -1, levels: int = 0):
        self.val = val
        self.next = [None] * levels  # 每层的下一个节点

class SkipList:
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level   # 最大层数
        self.p = p                   # 层数生成概率
        self.head = SkipNode(levels=self.max_level)
        self.level = 0               # 当前有效层数

    def _random_level(self) -> int:
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def search(self, target: int) -> bool:
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * (self.max_level)
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level, new_level):
                update[i] = self.head
            self.level = new_level
        new_node = SkipNode(num, new_level)
        for i in range(new_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        if not curr or curr.val != num:
            return False
        for i in range(self.level):
            if update[i].next[i] != curr:
                break
            update[i].next[i] = curr.next[i]
        while self.level > 0 and self.head.next[self.level-1] is None:
            self.level -= 1
        return True

# 使用示例
sl = SkipList()
sl.add(3)
sl.add(1)
sl.add(2)
print(sl.search(2))  # True
sl.erase(2)
print(sl.search(2))  # False
```

```go
package main

import (
	"math/rand"
	"time"
)

const (
	maxLevel = 16     // 最大层数
	p        = 0.5    // 层数生成概率
)

type SkipNode struct {
	val  int
	next []*SkipNode
}

type SkipList struct {
	head  *SkipNode
	level int
}

func NewSkipList() *SkipList {
	rand.Seed(time.Now().UnixNano())
	return &SkipList{
		head:  &SkipNode{next: make([]*SkipNode, maxLevel)},
		level: 0,
	}
}

func (sl *SkipList) randomLevel() int {
	level := 1
	for rand.Float64() < p && level < maxLevel {
		level++
	}
	return level
}

func (sl *SkipList) Search(target int) bool {
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < target {
			curr = curr.next[i]
		}
	}
	curr = curr.next[0]
	return curr != nil && curr.val == target
}

func (sl *SkipList) Add(num int) {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	newLevel := sl.randomLevel()
	if newLevel > sl.level {
		for i := sl.level; i < newLevel; i++ {
			update[i] = sl.head
		}
		sl.level = newLevel
	}
	newNode := &SkipNode{
		val:  num,
		next: make([]*SkipNode, newLevel),
	}
	for i := 0; i < newLevel; i++ {
		newNode.next[i] = update[i].next[i]
		update[i].next[i] = newNode
	}
}

func (sl *SkipList) Erase(num int) bool {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	curr = curr.next[0]
	if curr == nil || curr.val != num {
		return false
	}
	for i := 0; i < sl.level; i++ {
		if update[i].next[i] != curr {
			break
		}
		update[i].next[i] = curr.next[i]
	}
	for sl.level > 0 && sl.head.next[sl.level-1] == nil {
		sl.level--
	}
	return true
}

// 使用示例
func main() {
	sl := NewSkipList()
	sl.Add(3)
	sl.Add(1)
	sl.Add(2)
	println(sl.Search(2)) // true
	sl.Erase(2)
	println(sl.Search(2)) // false
}
```

### **跳表（Skip List）核心原理**
跳表是一种**多层链表结构**，通过建立多级索引实现快速查询（时间复杂度 $`O(\log n)`$），常用于代替平衡树。Redis 的有序集合（Sorted Set）底层即使用跳表。

#### **核心特性**
1. **多层结构**：包含多个层级的链表，底层链表包含所有元素，上层链表作为索引。
2. **随机层数**：插入节点时，随机生成层数（概率控制，通常为 50%）。
3. **快速查询**：从高层向低层逐级缩小范围，类似二分查找。

#### **时间复杂度**
| 操作    | 时间复杂度   |
|---------|-------------|
| 查找    | $`O(\log n)`$ |
| 插入    | $`O(\log n)`$ |
| 删除    | $`O(\log n)`$ |

### **关键操作解析**
| 操作       | 步骤                                                                 |
|------------|--------------------------------------------------------------------|
| **插入**   | 1. 查找插入位置并记录每层的前驱节点；<br>2. 随机生成层数；<br>3. 更新各层指针。 |
| **删除**   | 1. 查找目标节点并记录每层的前驱节点；<br>2. 更新指针并调整有效层数。           |
| **查找**   | 从最高层开始，逐层缩小范围，最终在底层定位。                               |

### **应用场景**
1. **有序集合**：如 Redis 的 `ZSET`，支持快速范围查询。
2. **替代平衡树**：实现简单且在高并发环境下性能更好。
3. **高性能索引**：需要频繁插入、删除和查询的场景。

通过跳表的结构设计和随机层数生成，可以在保证高效操作的同时避免复杂的平衡调整逻辑。

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

## 组合数

### **组合数求和公式**

#### **1. 全部组合数求和**
**公式**：
$$
\sum_{k=0}^n \binom{n}{k} = 2^n
$$

**解释**：
- **二项式定理**：根据二项式展开式，令 $` x = 1 `$：
  $`
  (1 + 1)^n = \sum_{k=0}^n \binom{n}{k} 1^k 1^{n-k} = \sum_{k=0}^n \binom{n}{k}.
  `$
  因此，和为 $` 2^n `$。

- **组合意义**：从 $` n `$ 个元素中选取任意多个元素（包括选 0 个或全选），总共有 $` 2^n `$ 种方式。

**示例**：
- 当 $` n = 3 `$ 时：
  $`
  \binom{3}{0} + \binom{3}{1} + \binom{3}{2} + \binom{3}{3} = 1 + 3 + 3 + 1 = 8 = 2^3.
  `$

#### **2. 带权组合数求和（每个组合乘以其元素个数）**
**公式**：
$$
\sum_{k=0}^n k \binom{n}{k} = n \cdot 2^{n-1}
$$

**解释**：
- **代数推导**：利用二项式定理的导数：
  $`
  \frac{d}{dx} \left( (1+x)^n \right) = n(1+x)^{n-1} = \sum_{k=0}^n k \binom{n}{k} x^{k-1}.
  `$
  两边乘以 $` x `$，再令 $` x = 1 `$，得：
  $`
  \sum_{k=0}^n k \binom{n}{k} = n \cdot 2^{n-1}.
  `$

- **组合意义**：从 $` n `$ 人中选一个委员会（任意大小），再选一个主席。总共有两种方式：
  1. 先选主席（$` n `$ 种选择），再从剩余 $` n-1 `$ 人中任意选成员（$` 2^{n-1} `$ 种）。
  2. 先选 $` k `$ 人（$` \binom{n}{k} `$ 种），再从 $` k `$ 人中选主席（$` k `$ 种），总数为 $` \sum_{k=0}^n k \binom{n}{k} `$。

**示例**：
- 当 $` n = 4 `$ 时：
  $`
  0\binom{4}{0} + 1\binom{4}{1} + 2\binom{4}{2} + 3\binom{4}{3} + 4\binom{4}{4} = 0 + 4 + 12 + 12 + 4 = 32 = 4 \cdot 2^{3}.
  `$

#### **3. 奇数、偶数组合数的和**
**公式**:
$$
\sum_{k=1}^{\lceil (n-1)/2 \rceil} \binom{n}{2k+1} = \sum_{k=0}^{\lceil (n-1)/2 \rceil} \binom{n}{2k} = 2^{n-1}
$$

由二项式展开可证

### **其他常见组合数求和公式**
1. **平方和公式**：
   $`
   \sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}.
   `$
   **解释**：从 $` 2n `$ 个元素中选 $` n `$ 个，等价于分成两组各 $` n `$ 个，并选 $` k `$ 个从第一组、$` n−k `$ 个从第二组。

2. **交替符号和**：
   $`
   \sum_{k=0}^n (-1)^k \binom{n}{k} = 0 \quad (n \geq 1).
   `$
   **解释**：由二项式定理 $` (1 - 1)^n = 0 `$。

### **总结**
| 求和类型                  | 公式                    | 核心推导工具       |
|---------------------------|-------------------------|--------------------|
| 全部组合数求和            | $` 2^n `$               | 二项式定理         |
| 带权组合数求和（元素个数） | $` n \cdot 2^{n-1} `$   | 导数或组合解释     |
| 平方和                    | $` \binom{2n}{n} `$     | 组合恒等式         |
| 交替符号和                | $` 0 `$（当 $` n \geq 1 `$） | 二项式定理代入负值 |

这些公式在概率论、组合优化和算法分析中有广泛应用，例如动态规划中的状态转移计数。

---

# 字符串

## 回文串

预处理

```go
package main

func handle(s string) [][]bool:
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, n)
		isPalindrome[i][i] = true
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			isPalindrome[i][j] = s[i] == s[j] && (i+2 >= j || isPalindrome[i+1][j-1])
		}
	}
    return isPalindrome
```

## KMP算法模板
```python
def kmp(s, pattern):
    # 构建next数组
    m = len(pattern)
    next_arr = [0]*m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        next_arr[i] = j
    
    # 匹配过程
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = next_arr[j-1]
        if s[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1
```

```go
package main

func kmp(s, pattern string) int {
    m := len(pattern)
    next := make([]int, m)
    j := 0
    for i := 1; i < m; i++ {
        for j > 0 && pattern[i] != pattern[j] {
            j = next[j-1]
        }
        if pattern[i] == pattern[j] {
            j++
        }
        next[i] = j
    }
    
    j = 0
    for i := 0; i < len(s); i++ {
        for j > 0 && s[i] != pattern[j] {
            j = next[j-1]
        }
        if s[i] == pattern[j] {
            j++
        }
        if j == m {
            return i - m + 1
        }
    }
    return -1
}
```

---

# 图论

## 存图方式

### 邻接矩阵

这是一种使用**二维矩阵**来进行存图的方式

适用于边数较多的**稠密图**使用，当边数量接近点数量的平方，即$`m = n^2`$，可定义为稠密图

```python
# 稠密图适用（节点编号0~n-1）
n = 5
graph = [[0]*n for _ in range(n)]

# 添加边（带权重）
graph[0][1] = 3  # 0→1的边权重为3
graph[1][2] = 2  # 1→2的边权重为2
```

### 邻接表

```go
package main

// 稀疏图适用
type Graph struct {
    nodes int
    edges [][]int // edges[i]存储节点i的所有邻接节点
}

func NewGraph(n int) *Graph {
    return &Graph{
        nodes: n,
        edges: make([][]int, n),
    }
}

// 添加无向边
func (g *Graph) AddEdge(u, v int) {
    g.edges[u] = append(g.edges[u], v)
    g.edges[v] = append(g.edges[v], u)
}
```

### 类存图（带权重）
```python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # 存储元组(node, weight)

# 构建示例
node0 = GraphNode(0)
node1 = GraphNode(1)
node0.neighbors.append((node1, 5))  # 0→1的边权重为5
```

## DFS

### 模板（Python）
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # 处理当前节点
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### 模板（Go）
```go
func dfs(node *GraphNode, visited map[*GraphNode]bool) {
    if visited[node] {
        return
    }
    visited[node] = true
    // 处理当前节点
    for _, neighbor := range node.neighbors {
        dfs(neighbor, visited)
    }
}
```

### 示例：岛屿数量
```python
def num_islands(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    def dfs(_i, _j):
        if 0 <= _i < rows and 0 <= _j < cols and grid[_i][_j] == '1':
            grid[_i][_j] = '0'
            dfs(_i+1, _j)
            dfs(_i-1, _j)
            dfs(_i, _j+1)
            dfs(_i, _j-1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

## BFS

- 核心思想
1. **队列结构**：用队列（先进先出）管理待访问的节点。
2. **逐层扩展**：按层处理节点，保证最先找到最短路径。
3. **避免重复访问**：记录已访问的节点（如哈希表、数组标记）。

### 基本结构（树/图的层序遍历）
```python
from collections import deque

def process(node):
    pass

def get_neighbors(node):
    return []

def bfs(start_node):
    queue = deque([start_node])  # 初始化队列
    visited = set()              # 记录已访问节点（图可能需要）
    visited.add(start_node)      # 标记初始节点
    
    while queue:
        level_size = len(queue)  # 当前层的节点数（层序遍历需要）
        for _ in range(level_size):
            node = queue.popleft()
            # 处理当前节点（如访问、判断目标等）
            process(node)
            # 遍历相邻节点（根据问题定义）
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return
```

### 示例：二叉树层序遍历
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# 测试
_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(_root))  # 输出 [[3], [9, 20], [15, 7]]
```

### 示例：网格最短路径（0 可走，1 障碍）
```python
from collections import deque

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右
    queue = deque([(start[0], start[1], 0)])     # (x, y, steps)
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    return -1  # 不可达

# 测试
_grid = [
    [0,0,1,0],
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0]
]
print(shortest_path(_grid, (0,0), (3,3)))  # 输出 6
```

### 基本结构（队列实现）
```go
package main

import (
    "container/list"
    "fmt"
)

// 树节点定义
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

// 层序遍历示例
func levelOrder(root *TreeNode) [][]int {
    result := [][]int{}
    if root == nil {
        return result
    }
    queue := list.New()
    queue.PushBack(root)
    
    for queue.Len() > 0 {
        levelSize := queue.Len()
        level := make([]int, 0, levelSize)
        for i := 0; i < levelSize; i++ {
            node := queue.Remove(queue.Front()).(*TreeNode)
            level = append(level, node.Val)
            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
        }
        result = append(result, level)
    }
    return result
}

// 测试
func main() {
    root := &TreeNode{3, 
        &TreeNode{9, nil, nil}, 
        &TreeNode{20, 
            &TreeNode{15, nil, nil}, 
            &TreeNode{7, nil, nil},
        },
    }
    fmt.Println(levelOrder(root)) // 输出 [[3] [9 20] [15 7]]
}
```

### 示例：网格最短路径
```go
type Point struct {
    x, y, steps int
}

func shortestPath(grid [][]int, start, end [2]int) int {
    rows, cols := len(grid), len(grid[0])
    directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    queue := list.New()
    visited := make(map[[2]int]bool)
    
    startX, startY := start[0], start[1]
    queue.PushBack(Point{startX, startY, 0})
    visited[[2]int{startX, startY}] = true
    
    for queue.Len() > 0 {
        front := queue.Front()
        queue.Remove(front)
        p := front.Value.(Point)
        if p.x == end[0] && p.y == end[1] {
            return p.steps
        }
        for _, dir := range directions {
            nx, ny := p.x + dir[0], p.y + dir[1]
            if nx >= 0 && nx < rows && ny >= 0 && ny < cols {
                if grid[nx][ny] == 0 && !visited[[2]int{nx, ny}] {
                    visited[[2]int{nx, ny}] = true
                    queue.PushBack(Point{nx, ny, p.steps + 1})
                }
            }
        }
    }
    return -1
}

// 测试
func main() {
    grid := [][]int{
        {0,0,1,0},
        {0,0,0,0},
        {1,1,0,1},
        {0,0,0,0},
    }
    fmt.Println(shortestPath(grid, [2]int{0,0}, [2]int{3,3})) // 输出 6
}
```

### BFS 关键点
| 特性        | 说明                                       |
|-----------|------------------------------------------|
| **时间复杂度** | O(N)，N 为节点数（每个节点访问一次）                    |
| **空间复杂度** | O(N)，最坏情况队列存储所有节点                        |
| **适用场景**  | 最短路径（无权图）、层序遍历、拓扑排序、连通块问题                |
| **注意事项**  | 1. 确保标记已访问节点；2. 处理空输入；3. 队列初始化正确；4. 边界检查 |

根据具体问题，调整 **节点定义**、**邻居获取方式** 和 **终止条件** 即可适配不同场景。

## 最短路径

### Dijkstra算法（优先队列实现）

```python
import heapq
from math import inf

def dijkstra(graph, start, n):
    dist: list[int] = [inf] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

```go
package main

import (
	"container/heap"
	"math"
)

func minTimeToReach(moveTime [][]int) int {
	n, m := len(moveTime), len(moveTime[0])
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, m)
		for j := range dist[i] {
			dist[i][j] = math.MaxInt32
		}
	}
	dist[0][0] = 0

	pq := &hp{}
	heap.Init(pq)
	heap.Push(pq, tuple{0, 0, 0})

	dirs := []int{-1, 0, 1, 0, -1}
	for {
		p := heap.Pop(pq).(tuple)
		d, i, j := p.dis, p.x, p.y

		if i == n-1 && j == m-1 {
			return d
		}
		if d > dist[i][j] {
			continue
		}

		for k := 0; k < 4; k++ {
			x, y := i+dirs[k], j+dirs[k+1]
			if x >= 0 && x < n && y >= 0 && y < m {
				t := max(moveTime[x][y], dist[i][j]) + 1
				if dist[x][y] > t {
					dist[x][y] = t
					heap.Push(pq, tuple{t, x, y})
				}
			}
		}
	}
}

type tuple struct{ dis, x, y int }
type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].dis < h[j].dis }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(tuple)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }
```


## 拓扑排序

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

## 数位dp

数位DP用于解决数字各位相关的计数问题，例如统计区间内满足特定条件的数字数量。其核心是通过动态规划逐位处理数字，利用记忆化技术避免重复计算。

#### **核心思想**
1. **拆解数位**：将数字转换为字符数组，逐位处理。
2. **状态记录**：记录当前位置、是否受上界限制、前导零状态及其他条件。
3. **记忆化搜索**：缓存已计算的状态，优化时间复杂度。

### **通用步骤**
1. **预处理数位**：将数字转换为字符串或数组。
2. **递归处理每一位**：
   - **限制条件**：当前位是否受上界限制。
   - **前导零处理**：标记是否处于前导零状态。
   - **状态转移**：根据当前位选择更新状态。
3. **边界处理**：处理完所有位后返回结果。

### **Python 模板（以统计无重复数字为例）**
```python
from functools import lru_cache

def count_special_numbers(n: int) -> int:
    s = str(n)
    
    @lru_cache(maxsize=None)
    def dp(pos: int, mask: int, tight: bool, lead: bool) -> int:
        if pos == len(s):
            return 0 if lead else 1
        
        limit = int(s[pos]) if tight else 9
        total = 0
        
        for d in range(0, limit + 1):
            new_tight = tight and (d == limit)
            new_lead = lead and (d == 0)
            
            if new_lead:
                total += dp(pos + 1, mask, new_tight, new_lead)
            else:
                if (mask & (1 << d)) == 0:
                    new_mask = mask | (1 << d)
                    total += dp(pos + 1, new_mask, new_tight, new_lead)
        
        return total
    
    return dp(0, 0, True, True)

# 示例：统计1到n中无重复数字的数目
print(count_special_numbers(20))  # 输出19（1-20中除11外都符合）
```

```go
package main

import (
	"fmt"
	"strconv"
)

func countSpecialNumbers(n int) int {
    s := strconv.Itoa(n)
    m := len(s)
    memo := make([][1 << 10]int, m)
    for i := range memo {
        for j := range memo[i] {
            memo[i][j] = -1 // -1 表示没有计算过
        }
    }
    var dfs func(int, int, bool, bool) int
    dfs = func(i, mask int, isLimit, isNum bool) (res int) {
        if i == m {
            if isNum {
                return 1 // 得到了一个合法数字
            }
            return
        }
        if !isLimit && isNum {
            p := &memo[i][mask]
            if *p >= 0 { // 之前计算过
                return *p
            }
            defer func() { *p = res }() // 记忆化
        }
        if !isNum { // 可以跳过当前数位
            res += dfs(i+1, mask, false, false)
        }
        d := 0
        if !isNum {
            d = 1 // 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        }
        up := 9
        if isLimit {
            up = int(s[i] - '0') // 如果前面填的数字都和 n 的一样，那么这一位至多填数字 s[i]（否则就超过 n 啦）
        }
        for ; d <= up; d++ { // 枚举要填入的数字 d
            if mask>>d&1 == 0 { // d 不在 mask 中，说明之前没有填过 d
                res += dfs(i+1, mask|1<<d, isLimit && d == up, true)
            }
        }
        return
    }
    return dfs(0, 0, true, false)
}
```

### **关键参数解释**
| 参数    | 说明                                                                 |
|---------|--------------------------------------------------------------------|
| `pos`   | 当前处理的数位位置（从高位到低位）。                                      |
| `mask`  | 状态掩码，记录已使用的数字（例如用位掩码表示）。                             |
| `tight` | 是否受上界限制（如处理到第`i`位时，前`i-1`位是否与上界相同）。                 |
| `lead`  | 是否处于前导零状态（前导零不计入已使用数字）。                              |


### **适用场景**
1. **无重复数字计数**：如示例所示。
2. **数位和限制**：统计数位和等于特定值的数字。
3. **特定模式匹配**：如包含/不包含某些子序列。


通过合理设计状态转移和记忆化策略，数位DP能高效解决复杂的数位计数问题。模板可根据具体问题调整状态定义和转移逻辑。

### 模板 2.0

```python
from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))  # 避免在 dfs 中频繁调用 int()
        n = len(high)
        low = list(map(int, str(start).zfill(n)))  # 补前导零，和 high 对齐
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            if i < diff:  # 枚举这个数位填什么
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # 这个数位只能填 s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= hi:  # 题目保证 x <= limit，无需判断
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)
```

```go
package main

func numberOfPowerfulInt(start, finish int64, limit int, s string) int64 {
	low := strconv.FormatInt(start, 10)
	high := strconv.FormatInt(finish, 10)
	n := len(high)
	low = strings.Repeat("0", n-len(low)) + low // 补前导零，和 high 对齐
	diff := n - len(s)

	memo := make([]int64, n)
	for i := range memo {
		memo[i] = -1
	}
	var dfs func(int, bool, bool) int64
	dfs = func(i int, limitLow, limitHigh bool) (res int64) {
		if i == n {
			return 1
		}
		
		if !limitLow && !limitHigh {
			p := &memo[i]
			if *p >= 0 {
				return *p
			}
			defer func() { *p = res }()
		}

		// 第 i 个数位可以从 lo 枚举到 hi
		// 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
		lo := 0
		if limitLow {
			lo = int(low[i] - '0')
		}
		hi := 9
		if limitHigh {
			hi = int(high[i] - '0')
		}

		if i < diff { // 枚举这个数位填什么
			for d := lo; d <= min(hi, limit); d++ {
				res += dfs(i+1, limitLow && d == lo, limitHigh && d == hi)
			}
		} else { // 这个数位只能填 s[i-diff]
			x := int(s[i-diff] - '0')
			if lo <= x && x <= hi { // 题目保证 x <= limit，无需判断
				res += dfs(i+1, limitLow && x == lo, limitHigh && x == hi)
			}
		}
		return
	}
	return dfs(0, true, true)
}
```

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
def combination_sum(candidates, target: int):
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
def combination_sum2(candidates, target: int):
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


## 倍增

倍增（Doubling）是一种**预处理数据并利用二进制思想优化查询效率**的算法技术。其核心思想是通过构建一个**跳转表**（如稀疏表，Sparse Table），使得每次查询或操作的时间复杂度从线性降低到对数级别（如 $`O(\log n)`$。以下是其核心要点和应用场景：

### **倍增的核心原理**
1. **二进制分解**  
   将问题分解为多个**按指数递增的步长**（如 $`2^0, 2^1, 2^2, \dots`$）来处理。例如，跳转表中存储从每个位置出发，经过 $`2^k`$ 步后的结果。
   
2. **预处理跳转表**  
   构建一个二维数组 `dp[k][i]`，表示从位置 `i` 出发，跳转 $`2^k`$ 步后的目标位置或计算结果。例如：
   - `dp[0][i]` 表示跳转 1 步（$`2^0 = 1`$）后的结果。
   - `dp[k][i] = dp[k-1][ dp[k-1][i] ]`，即通过递归方式构建跳转表。

3. **快速查询**  
   将目标步长分解为二进制形式，按位累加跳转步长。例如，跳转 13 步（二进制 `1101`）时，分解为 $`8 + 4 + 1`$ 步，依次跳转 $`2^3, 2^2, 2^0`$ 步。

### **典型应用场景**
#### 1. **最近公共祖先（LCA）**
   - **问题**：在树中快速找到两个节点的最近公共祖先。
   - **倍增实现**：
     1. 预处理每个节点的 $`2^k`$ 级祖先（`up[k][u]`）。
     2. 先将两个节点调整到同一深度，再同时向上跳转，直到找到公共祖先。
   - **时间复杂度**：预处理 $`O(n \log n)`$，查询 $`O(\log n)`$。

```python
from typing import List

class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return self.pa[x][0]
```
```go
pacakge main

type TreeAncestor struct {
    depth []int
    pa    [][]int
}

func Constructor(edges [][]int) *TreeAncestor {
    n := len(edges) + 1
    m := bits.Len(uint(n))
    g := make([][]int, n)
    for _, e := range edges {
        x, y := e[0], e[1] // 节点编号从 0 开始
        g[x] = append(g[x], y)
        g[y] = append(g[y], x)
    }

    depth := make([]int, n)
    pa := make([][]int, n)
    var dfs func(int, int)
    dfs = func(x, fa int) {
        pa[x] = make([]int, m)
        pa[x][0] = fa
        for _, y := range g[x] {
            if y != fa {
                depth[y] = depth[x] + 1
                dfs(y, x)
            }
        }
    }
    dfs(0, -1)

    for i := range m - 1 {
        for x := range n {
            if p := pa[x][i]; p != -1 {
                pa[x][i+1] = pa[p][i]
            } else {
                pa[x][i+1] = -1
            }
        }
    }
    return &TreeAncestor{depth, pa}
}

func (t *TreeAncestor) GetKthAncestor(node, k int) int {
    for ; k > 0; k &= k - 1 {
        node = t.pa[node][bits.TrailingZeros(uint(k))]
    }
    return node
}

// 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
func (t *TreeAncestor) GetLCA(x, y int) int {
    if t.depth[x] > t.depth[y] {
        x, y = y, x
    }
    y = t.GetKthAncestor(y, t.depth[y]-t.depth[x]) // 使 y 和 x 在同一深度
    if y == x {
        return x
    }
    for i := len(t.pa[x]) - 1; i >= 0; i-- {
        px, py := t.pa[x][i], t.pa[y][i]
        if px != py {
            x, y = px, py // 同时往上跳 2^i 步
        }
    }
    return t.pa[x][0]
}
```

#### 2. **区间最值查询（RMQ）**
   - **问题**：多次查询数组某个区间的最小值/最大值。
   - **倍增实现**：
     1. 构建稀疏表 `st[k][i]`，表示从 `i` 开始长度为 $`2^k`$ 的区间最值。
     2. 查询区间 `[L, R]` 时，取最大的 $`k`$ 使得 $`2^k \leq R-L+1`$，比较 `st[k][L]` 和 `st[k][R-2^k+1]`。
   - **时间复杂度**：预处理 $`O(n \log n)`$，查询 $`O(1)`$。

#### 3. **快速幂**
   - **问题**：高效计算 $`a^b \mod p`$。
   - **倍增实现**：
     1. 将指数 $`b`$ 分解为二进制形式。
     2. 通过累乘 $`a^{2^k}`$ 快速计算结果。
   - **时间复杂度**：$`O(\log b)`$。

快速幂算法用于高效计算大整数幂或幂取模，时间复杂度为 $`O(\log n)`$。

#### **Python 模板**
```python
def fast_power(a: int, b: int, mod: int = None) -> int:
    """
    计算 a^b 或 (a^b) % mod
    :param a: 底数
    :param b: 指数（非负整数）
    :param mod: 可选模数
    :return: a^b 或 (a^b) % mod
    """
    result = 1
    a = a % mod if mod else a  # 初始取模（若提供mod）
    while b > 0:
        if b % 2 == 1:  # 当前二进制位为1
            result = result * a
            if mod: result %= mod
        a = a * a       # 基数平方
        if mod: a %= mod
        b //= 2         # 右移一位
    return result

# 示例
print(fast_power(2, 10))          # 输出 1024
print(fast_power(2, 10, 1000))    # 输出 24 (1024 % 1000)
```

```go
package main

import "fmt"

func fastPower(a, b, mod int) int {
    result := 1
    a = a % mod // 初始取模（若mod > 0）
    for b > 0 {
        if b%2 == 1 { // 当前二进制位为1
            result = (result * a) % mod
        }
        a = (a * a) % mod // 基数平方
        b /= 2           // 右移一位
    }
    return result
}

func main() {
    fmt.Println(fastPower(2, 10, 0))    // 输出 1024（mod=0时不取模）
    fmt.Println(fastPower(2, 10, 1000)) // 输出 24
}
```

##### 矩阵快速幂

矩阵快速幂是一种高效解决线性递推问题的算法，通过将递推关系转化为矩阵乘法形式，利用快速幂将时间复杂度从 $`O(n)`$ 优化到 $`O(\log n)`$。以下是其核心原理和实现方法：

**通用步骤**

**1. 确定递推阶数**

对于 $`k`$ 阶线性递推（如 $`F(n) = a_1F(n-1) + \dots + a_kF(n-k)`$），构造 $`k \times k`$ 的转移矩阵。

**2. 构造转移矩阵**

- 第 $`i`$ 行表示如何从 $`F(n-i)`$ 推导到 $`F(n-i+1)`$。
- 例如，斐波那契数列的转移矩阵为：
$$
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
$$

**3. 初始状态向量**

根据递推的初始条件定义初始向量：
$$
\text{初始状态} = 
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

**4. 计算矩阵幂**

通过快速幂计算 $`\text{转移矩阵}^{n}`$，再与初始状态相乘得到结果。

```go
func fib(n int) int {
    if n == 0 {
        return 0
    }
    // 转移矩阵
    mat := [][]int{{1, 1}, {1, 0}}
    // 计算 mat^(n-1)
    res := matrixPower(mat, n-1)
    // 初始状态 [F(1), F(0)] = [1, 0]
    return res[0][0] * 1 + res[0][1] * 0
}
```

**应用场景**
1. **线性递推问题**：如斐波那契数列、爬楼梯问题。
2. **动态规划优化**：将状态转移方程转化为矩阵形式。
3. **图论中的路径计数**：邻接矩阵的幂表示路径数。

**推广到 k 阶递推**

对于 $`k`$ 阶递推 $`F(n) = a_1F(n-1) + a_2F(n-2) + \dots + a_kF(n-k)`$，转移矩阵为：
$$
\begin{bmatrix}
a_1 & a_2 & \dots & a_{k-1} & a_k \\
1 & 0 & \dots & 0 & 0 \\
0 & 1 & \dots & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & 0
\end{bmatrix}
$$
初始状态向量为：
$$
\begin{bmatrix}
F(k-1) \\
F(k-2) \\
\vdots \\
F(0)
\end{bmatrix}
$$

1. **构造矩阵**：将递推关系转化为矩阵乘法形式。
2. **快速幂加速**：通过矩阵快速幂将线性递推的时间复杂度优化到对数级。
3. **通用性强**：适用于任何线性递推关系，只需调整转移矩阵和初始状态。

```python
from typing import List


# 矩阵快速幂
# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]], mod: int) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*b)]
            for row in a]


# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]], mod: int = 1000_000_007) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res, mod)
        a = mul(a, a, mod)
        n >>= 1
    return res
```

### **优势与局限**
- **优势**：将线性时间的查询优化到对数时间。
- **局限**：需要额外的空间存储跳转表（如 $`O(n \log n)`$ 的稀疏表）。
- **适用场景**：适用于**静态数据**（预处理后数据不变）的多次查询问题。

理解倍增的核心在于掌握**二进制分解**和**跳转表的预处理逻辑**，它是高效解决许多算法问题的关键技巧。

----