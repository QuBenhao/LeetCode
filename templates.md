**算法模板**

# 目录

1. [二分查找](#二分查找)
    - [带重复元素的旋转数组](#带重复元素的旋转数组)
2. [堆](#堆)
    - [优先队列](#优先队列)
3. [字典树](#trie)
4. [单调栈](#单调栈)
5. [滑动窗口](#滑动窗口)
6. [双指针](#双指针)
7. [深度优先搜索](#DFS)
8. [广度优先搜索](#BFS)
9. [拓扑排序](#拓扑排序)
10. [二进制](#二进制)
11. [动态规划](#动态规划)
    - [回文串切割](#回文串切割)
12. [并查集](#并查集)
13. [树状数组](#树状数组)
14. [线段树](#线段树)
15. [数学](#数学)
    - [费马平方和定理](#费马平方和定理)
16. [链表](#链表)
17. [二叉树](二叉树)
18. [字符串](#字符串)
19. [回溯](#回溯)
    - [N皇后](#N皇后)
    - [排列组合](#排列组合)
        - [全排列](#全排列)
        - [重复元素全排列](#重复元素全排列)
        - [组合](#组合)
        - [重复元素组合](#重复元素组合)
        - [重复元素子集](#重复元素子集)

# 二分查找

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

## 带重复元素的旋转数组

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

# 单调栈

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

# 滑动窗口

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

# 双指针

# DFS

# BFS

# 拓扑排序

# 二进制

# 动态规划

## 回文串切割
```python
def minCut(s):
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

# 并查集

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

# 树状数组

# 线段树

# 数学

## 费马平方和定理

### 定理内容

一个奇素数$`p`$, 可以表示为两个整数的平方和（即$`p = x^2 + y^2`$），当且仅当$$p \equiv 1 \pmod{4}$$

### 证明思路（简述）
如果$`p \equiv 1 \pmod{4}`$，可以通过数论方法证明$`p`$可以表示为两个平方数之和。
如果$`p \equiv 3 \pmod{4}`$，则$`p`$无法表示为两个平方数之和。

### 示例
$`5 = 2^2 + 1^2`$，且$`5 \equiv 1 \pmod{4}`$

$`13 = 3^2 + 2^2`$，且$`13 \equiv 1 \pmod{4}`$

$`7`$无法表示为两个平方数之和，因为$`7 \equiv 3 \pmod{4}`$


# 链表

# 二叉树

# 字符串

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