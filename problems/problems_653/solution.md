# [Python/Java/JavaScript/Go] 迭代器 + 双指针

> slug: pythonjavajavascriptgo-by-himymben-prb2
> date: 2022-03-20
> tags: Go, Java, JavaScript, Python, Python3
> question: Two Sum IV - Input is a BST (two-sum-iv-input-is-a-bst)
> url: https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/solutions/zd2FLs/pythonjavajavascriptgo-by-himymben-prb2/

---
### 解题思路
如果我们有一个从小到大的排列好的数组，那么我们找两数之和的方案就很简单了，一个指针从左往右扫，一个指针从右往左扫。
当左指针与右指针的和小于目标时，左指针右移；
当左指针与右指针的和大于目标时，右指针左移；
当左指针与右指针的和等于目标时，我们找到了想要的结果。

而这个从小到大的数组，从BST的中序遍历便可以得到。
怎么在不遍历完就模拟出两个指针的情况呢？
我们需要用到迭代器。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def in_order(node):
            if node:
                yield from in_order(node.left)
                yield node.val
                yield from in_order(node.right)
        
        def in_order_reverse(node):
            if node:
                yield from in_order_reverse(node.right)
                yield node.val
                yield from in_order_reverse(node.left)
        
        left_gen, right_gen = in_order(root), in_order_reverse(root)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            if left + right < k:
                left = next(left_gen)
            elif left + right > k:
                right = next(right_gen)
            else:
                return True
        return False
```
```Java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        BSTIterator leftGen = new BSTIterator(root);
        BSTIteratorReverse rightGen = new BSTIteratorReverse(root);
        int left = leftGen.next(), right = rightGen.next();
        while(left < right) {
            if(left + right < k)
                left = leftGen.next();
            else if(left + right > k)
                right = rightGen.next();
            else
                return true;
        }
        return false;
    }

    private static class BSTIterator {
        private TreeNode cur;
        private Deque<TreeNode> stack;

        public BSTIterator(TreeNode root) {
            cur = root;
            stack = new LinkedList<TreeNode>();
        }
        
        public int next() {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            int ret = cur.val;
            cur = cur.right;
            return ret;
        }
    }

    private static class BSTIteratorReverse {
        private TreeNode cur;
        private Deque<TreeNode> stack;

        public BSTIteratorReverse(TreeNode root) {
            cur = root;
            stack = new LinkedList<TreeNode>();
        }
        
        public int next() {
            while (cur != null) {
                stack.push(cur);
                cur = cur.right;
            }
            cur = stack.pop();
            int ret = cur.val;
            cur = cur.left;
            return ret;
        }
    }
}
```
```JavaScript []
var BSTIterator = function(root) {
    this.cur = root;
    this.stack = [];
};

BSTIterator.prototype.next = function() {
    while (this.cur) {
        this.stack.push(this.cur);
        this.cur = this.cur.left;
    }
    this.cur = this.stack.pop();
    const ret = this.cur.val;
    this.cur = this.cur.right;
    return ret;
};

var BSTIteratorReverse = function(root) {
    this.cur = root;
    this.stack = [];
};

BSTIteratorReverse.prototype.next = function() {
    while (this.cur) {
        this.stack.push(this.cur);
        this.cur = this.cur.right;
    }
    this.cur = this.stack.pop();
    const ret = this.cur.val;
    this.cur = this.cur.left;
    return ret;
};

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
    const leftGen = new BSTIterator(root), rightGen = new BSTIteratorReverse(root)
    let left = leftGen.next(), right = rightGen.next()
    while(left < right) {
        if(left + right < k)
            left = leftGen.next()
        else if(left + right > k)
            right = rightGen.next()
        else
            return true
    }
    return false
};
```
```Go []
type BSTIterator struct {
    stack []*TreeNode
    cur   *TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
    return BSTIterator{cur: root}
}

func (it *BSTIterator) Next() int {
    for node := it.cur; node != nil; node = node.Left {
        it.stack = append(it.stack, node)
    }
    it.cur, it.stack = it.stack[len(it.stack)-1], it.stack[:len(it.stack)-1]
    val := it.cur.Val
    it.cur = it.cur.Right
    return val
}

type BSTIteratorReverse struct {
    stack []*TreeNode
    cur   *TreeNode
}

func Const(root *TreeNode) BSTIteratorReverse {
    return BSTIteratorReverse{cur: root}
}

func (it *BSTIteratorReverse) Next() int {
    for node := it.cur; node != nil; node = node.Right {
        it.stack = append(it.stack, node)
    }
    it.cur, it.stack = it.stack[len(it.stack)-1], it.stack[:len(it.stack)-1]
    val := it.cur.Val
    it.cur = it.cur.Left
    return val
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTarget(root *TreeNode, k int) bool {
    leftGen, rightGen := Constructor(root), Const(root)
    for left, right := leftGen.Next(), rightGen.Next(); left < right; {
        if v := left + right; v == k {
            return true
        } else if v < k {
            left = leftGen.Next()
        } else {
            right = rightGen.Next()
        }
    }
    return false
}
```