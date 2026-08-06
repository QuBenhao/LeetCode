# [Go] 新学会的线段树，来练一练

> slug: go-xin-xue-hui-by-himymben-uxjd
> date: 2022-04-05
> tags: Go
> question: Longest Substring of One Repeating Character (longest-substring-of-one-repeating-character)
> url: https://leetcode.cn/problems/longest-substring-of-one-repeating-character/solutions/WWkiyv/go-xin-xue-hui-by-himymben-uxjd/

---
### 解题思路
从昨天的[307](https://leetcode.cn/problems/range-sum-query-mutable/solution/pythonjavajavascriptgo-xian-duan-shu-mo-kmpw3/)魔改的。
其实就是区间和变为区间最大值，唯一重点是头尾字符可能发生合并而增加长度，可能要更新区间最大值。
Python超时了，和Go逻辑一模一样我也是很无语

### 代码

```golang []
func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
    segmentTree, n := Constructor(s), len(queryCharacters)
    ans := make([]int, n)
    for i := 0; i < n; i++ {
        segmentTree.UpdateTree(1, queryIndices[i] + 1, queryCharacters[i])
        ans[i] = segmentTree.Query(1, 1, len(s))
    }
    return ans
}

type Node struct {
    l, r, max, pl, sl int
    pre, suf byte
}

func Constructor_Node(l, r int) Node {
    return Node{l, r, 0, 0, 0, 'a', 'a'}
}

type NumArray struct {
    tr []Node
}


func Constructor(nums string) NumArray {
    n := len(nums)
    tr := make([]Node, n * 4)
    obj := NumArray{tr}
    obj.Build(1, 1, n)
    for i := range nums {
        obj.UpdateTree(1, i + 1, nums[i])
    }
    return obj
}

func (this *NumArray) Build(u, l, r int) {
    this.tr[u] = Constructor_Node(l, r)
    if l < r {
        mid := (l + r) >> 1
        this.Build(u << 1, l, mid)
        this.Build(u << 1 | 1, mid + 1, r)
    }
}

func (this *NumArray) UpdateTree(u, x int, v byte) {
    if this.tr[u].l == x && this.tr[u].r == x {
        this.tr[u].pre = v
        this.tr[u].pl = 1
        this.tr[u].suf = v
        this.tr[u].sl = 1
        this.tr[u].max = 1
        return
    }
    mid := (this.tr[u].l + this.tr[u].r) >> 1
    if x <= mid {
        this.UpdateTree(u << 1, x, v)
    } else {
        this.UpdateTree(u << 1 | 1, x, v)
    }
    this.Pushup(u)
}

func (this *NumArray) Query(u, l, r int) (ans int) {
    if l <= this.tr[u].l && this.tr[u].r <= r {
        return this.tr[u].max
    }
    mid := (this.tr[u].l + this.tr[u].r) >> 1
    if l <= mid {
        ans += this.Query(u << 1, l, r)
    }
    if r > mid {
        ans += this.Query(u << 1 | 1, l, r)
    }
    return
}

func (this *NumArray) Pushup(u int) {
    left, right := this.tr[u << 1], this.tr[u << 1 | 1]
    if left.suf == right.pre {
        this.tr[u].max = max(max(left.max, right.max), left.sl + right.pl)
    } else {
        this.tr[u].max = max(left.max, right.max)
    }
    this.tr[u].pre = left.pre
    this.tr[u].pl = left.pl
    if left.pl == left.r - left.l + 1 && left.suf == right.pre {
        this.tr[u].pl += right.pl
    }
    this.tr[u].suf = right.suf
    this.tr[u].sl = right.sl
    if right.sl == right.r - right.l + 1 && right.pre == left.suf {
        this.tr[u].sl += left.sl
    }
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
```Python3 []
# 此代码还超时中
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        segment_tree = Tree(s)
        ans = []
        for i, idx in enumerate(queryIndices):
            segment_tree.update_tree(1, idx + 1, queryCharacters[i])
            ans.append(segment_tree.query(1, 1, len(s)))
        return ans


class Node:
    def __init__(self, l, r):
        self.l, self.r = l, r
        self.pre = ['', 0]
        self.suf = ['', 0]
        self.max = 0
    
    def __str__(self):
        return f"l: {self.l}, r: {self.r}, pre: {self.pre}, suf: {self.suf}, max: {self.max}"

class Tree:

    def __init__(self, s: str):
        n = len(s)
        self.tr = [None] * (4 * n)
        self.build(1, 1, n)
        for i, c in enumerate(s):
            self.update_tree(1, i + 1, c)

    def build(self, u, l, r):
        self.tr[u] = Node(l, r)
        if l < r:
            mid = (l + r) >> 1
            self.build(u << 1, l, mid)
            self.build(u << 1 | 1, mid + 1, r)
    
    def update_tree(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].pre = [v, 1]
            self.tr[u].suf = [v, 1]
            self.tr[u].max = 1
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.update_tree(u << 1, x, v)
        else:
            self.update_tree(u << 1 | 1, x, v)
        self.pushup(u)
    
    def query(self, u, l, r):
        if l <= self.tr[u].l and self.tr[u].r <= r:
            return self.tr[u].max
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        ans = 0
        if l <= mid:
            ans = max(ans, self.query(u << 1, l, r))
        if r > mid:
            ans = max(ans, self.query(u << 1 | 1, l, r))
        return ans
    
    def pushup(self, u):
        left, right = self.tr[u << 1], self.tr[u << 1 | 1]
        if left.suf[0] == right.pre[0]:
            # 合并
            self.tr[u].max = max(left.max, right.max, left.suf[1] + right.pre[1])
        else:
            self.tr[u].max = max(left.max, right.max)
        self.tr[u].pre[0] = left.pre[0]
        self.tr[u].pre[1] = left.pre[1]
        if left.pre[1] == left.r - left.l + 1:
            if left.suf[0] == right.pre[0]:
                self.tr[u].pre[1] += right.pre[1]
        self.tr[u].suf[0] = right.suf[0]
        self.tr[u].suf[1] = right.suf[1]
        if right.suf[1] == right.r - right.l + 1:
            if right.pre[0] == left.suf[0]:
                self.tr[u].suf[1] += left.suf[1]

```