# [Python/Java/JavaScript/Go] 线段树模版

> slug: pythonjavajavascriptgo-xian-duan-shu-mo-kmpw3
> date: 2022-04-04
> tags: Go, Java, JavaScript, Python, Python3
> question: Range Sum Query - Mutable (range-sum-query-mutable)
> url: https://leetcode.cn/problems/range-sum-query-mutable/solutions/BRllMg/pythonjavajavascriptgo-xian-duan-shu-mo-kmpw3/

---
### 解题思路

从[叶总](https://leetcode.cn/problems/range-sum-query-mutable/solution/by-ac_oier-zmbn/)那里学了一下线段树，方便以后复制粘贴。
我说一下我的理解。

根节点是tr[1]，所以我们总是从1出发开始构造或更新还有查询。
左节点是自己乘2，右节点是自己乘二加一，也就是`u -> u << 1`和`u -> u << 1 | 1`。
在更新区间变化时，更新增量`val - self.nums[index]`。
底层更新完区间和之后，回调更新上层的区间和`pushup`。
查询时，如果一个区间范围被覆盖，直接返回这个区间的和，否则向下递归找到被查询区间覆盖的区间，统计所有区间的和。

### 代码

```Python3 []
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tr = [None] * (4 * n)
        self.nums = nums
        self.build(1, 1, n)
        for i, num in enumerate(nums):
            self.update_tree(1, i + 1, num)

    def update(self, index: int, val: int) -> None:
        self.update_tree(1, index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, left + 1, right + 1)

    def build(self, u, l, r):
        self.tr[u] = Node(l, r)
        if l < r:
            mid = (l + r) >> 1
            self.build(u << 1, l, mid)
            self.build(u << 1 | 1, mid + 1, r)
    
    def update_tree(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].v += v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.update_tree(u << 1, x, v)
        else:
            self.update_tree(u << 1 | 1, x, v)
        self.pushup(u)
    
    def query(self, u, l , r):
        if l <= self.tr[u].l and self.tr[u].r <= r:
            return self.tr[u].v
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        ans = 0
        if l <= mid:
            ans += self.query(u << 1, l, r)
        if r > mid:
            ans += self.query(u << 1 | 1, l, r)
        return ans
    
    def pushup(self, u):
        self.tr[u].v = self.tr[u << 1].v + self.tr[u << 1 | 1].v

class Node:
    def __init__(self, l, r):
        self.l, self.r = l, r
        self.v = 0


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```
```Java []
/**
作者：AC_OIer
链接：https://leetcode.cn/problems/range-sum-query-mutable/solution/by-ac_oier-zmbn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
class NumArray {
    Node[] tr;
    class Node {
        int l, r, v;
        Node(int _l, int _r) {
            l = _l; r = _r;
        }
    }
    void build(int u, int l, int r) {
        tr[u] = new Node(l, r);
        if (l == r) return;
        int mid = l + r >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
    }
    void update(int u, int x, int v) {
        if (tr[u].l == x && tr[u].r == x) {
            tr[u].v += v;
            return ;
        }
        int mid = tr[u].l + tr[u].r >> 1;
        if (x <= mid) update(u << 1, x, v);
        else update(u << 1 | 1, x, v);
        pushup(u);
    }
    int query(int u, int l, int r) {
        if (l <= tr[u].l && tr[u].r <= r) return tr[u].v;
        int mid = tr[u].l + tr[u].r >> 1;
        int ans = 0;
        if (l <= mid) ans += query(u << 1, l, r);
        if (r > mid) ans += query(u << 1 | 1, l, r);
        return ans;
    }
    void pushup(int u) {
        tr[u].v = tr[u << 1].v + tr[u << 1 | 1].v;
    }

    int[] nums;
    public NumArray(int[] _nums) {
        nums = _nums;
        int n = nums.length;
        tr = new Node[n * 4];
        build(1, 1, n);
        for (int i = 0; i < n; i++) update(1, i + 1, nums[i]);
    }
    public void update(int index, int val) {
        update(1, index + 1, val - nums[index]);
        nums[index] = val;
    }
    public int sumRange(int left, int right) {
        return query(1, left + 1, right + 1);
    }
}
```
```JavaScript []
var Node = function(l, r) {
    this.l = l
    this.r = r
    this.v = 0
}

/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    const n = nums.length
    this.tr = new Array(n * 4)
    this.nums = nums
    this.build(1, 1, n)
    for(let i = 0; i < n; i++)
        this.update_tree(1, i + 1, nums[i])
};

NumArray.prototype.build = function(u, l, r) {
    this.tr[u] = new Node(l, r)
    if(l < r) {
        const mid = l + r >> 1
        this.build(u << 1, l, mid)
        this.build(u << 1 | 1, mid + 1, r)
    }
}

NumArray.prototype.update_tree = function(u, x, v) {
    if(this.tr[u].l == x && this.tr[u].r == x) {
        this.tr[u].v += v
        return
    }
    const mid = this.tr[u].l + this.tr[u].r >> 1
    if(x <= mid)
        this.update_tree(u << 1, x, v)
    else
        this.update_tree(u << 1 | 1, x, v)
    this.pushup(u)
}

NumArray.prototype.query = function(u, l, r) {
    if(l <= this.tr[u].l && this.tr[u].r <= r)
        return this.tr[u].v
    let ans = 0
    const mid = this.tr[u].l + this.tr[u].r >> 1
    if(l <= mid)
        ans += this.query(u << 1, l, r)
    if(mid < r)
        ans += this.query(u << 1 | 1, l, r)
    return ans
}

NumArray.prototype.pushup = function(u) {
    this.tr[u].v = this.tr[u << 1].v + this.tr[u << 1 | 1].v
}

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(index, val) {
    this.update_tree(1, index + 1, val - this.nums[index])
    this.nums[index] = val
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    return this.query(1, left + 1, right + 1)
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */
```
```Go []
type Node struct {
    l, r, v int
}

func Constructor_Node(l, r int) Node {
    return Node{l, r, 0}
}

type NumArray struct {
    nums []int
    tr []Node
}


func Constructor(nums []int) NumArray {
    n := len(nums)
    tr := make([]Node, n * 4)
    obj := NumArray{nums, tr}
    obj.Build(1, 1, n)
    for i, num := range nums {
        obj.UpdateTree(1, i + 1, num)
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

func (this *NumArray) UpdateTree(u, x, v int) {
    if this.tr[u].l == x && this.tr[u].r == x {
        this.tr[u].v += v
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
        return this.tr[u].v
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
    this.tr[u].v = this.tr[u << 1].v + this.tr[u << 1 | 1].v
}

func (this *NumArray) Update(index int, val int)  {
    this.UpdateTree(1, index + 1, val - this.nums[index])
    this.nums[index] = val
}


func (this *NumArray) SumRange(left int, right int) int {
    return this.Query(1, left + 1, right + 1)
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
```