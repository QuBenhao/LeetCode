**算法模板**

# 目录

1. [二分查找](#二分查找)
2. [堆](#堆)
3. [字典树](#trie)
4. [单调栈](#单调栈)
5. [滑动窗口](#滑动窗口)
6. [双指针](#双指针)
7. [深度优先搜索](#DFS)
8. [广度优先搜索](#BFS)
9. [拓扑排序](#拓扑排序)
10. [二进制](#二进制)
11. [动态规划](#动态规划)
12. [并查集](#并查集)
13. [树状数组](#树状数组)
14. [线段树](#线段树)
15. [数学](#数学)
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

# 二分查找

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