# 1569. 将子数组重新排序得到同一个二叉搜索树的方案数

> date: 2026-10-18
> tags: Python3, 二叉搜索树, 组合计数, 分治
> question: Number of Ways to Reorder Array to Get Same BST (number-of-ways-to-reorder-array-to-get-same-bst)
> url: https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/

---

> Problem: [1569. 将子数组重新排序得到同一个二叉搜索树的方案数](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/)

## 结论

记 `ls`、`rs` 为左右子树的节点数，`f` 为合法排列数：

```text
f(nil) = 1
f(node) = C(ls + rs, ls) × f(left) × f(right)
answer  = f(root) - 1
```

整道题只有两个判断题：**哪些重排是合法的**，**左右子树合并时为什么是乘组合数**。下面分别解决。

## 一、合法重排 ＝ 满足「父先于子」的排列

必要性：`y` 要挂到 `x` 的子树里，插入 `y` 的那一刻 `x` 必须在树上，也就是 `x` 在序列里排在 `y` 之前。

充分性：`y` 的插入路径只由「从根到 `y` 的父亲」这一串祖先与 `y` 的大小比较决定，跟其它节点是否已经插入无关。只要每个祖先都排在 `y` 前面，路径就完全复现，落点相同，整棵树同形。

所以约束**只有**「每个节点排在它的所有后代之前」，这正是能分治的前提。

## 二、左右子树互不干扰

左子树的元素全部小于根，插入时只会与左子树内的节点比较；右子树同理。两者的元素在「父先于子」上各自受约束，**彼此之间没有任何顺序要求**。于是合并时只需决定「谁占哪些位置」，不用管「谁先谁后」。

## 三、合并时为什么是 C(ls + rs, ls)

根固定占据第一个位置。剩下 `ls + rs` 个空位里：

- 选 `ls` 个给左子树 —— `C(ls + rs, ls)` 种，这一步只选位置，不管内容；
- 左子树内部怎么排 —— `f(left)` 种；
- 右子树内部怎么排 —— `f(right)` 种。

三个选择彼此独立，所以连乘。

最容易漏的就是第一个因子：只写 `f(left) × f(right)`，等于假设「左半边整体在前、右半边整体在后」，只数了一种交错方式。**必须乘 `C(ls + rs, ls)`。**

## 四、示例：nums = [3, 4, 5, 1, 2]

建树后根为 3，左子树 `{1, 2}`、右子树 `{4, 5}`，两棵子树各只有 1 种排法，合并方式 `C(4, 2) = 6`：

```text
3, 1, 2, 4, 5
3, 1, 4, 2, 5
3, 1, 4, 5, 2
3, 4, 1, 2, 5
3, 4, 1, 5, 2
3, 4, 5, 1, 2   ← 原数组本身
```

去掉最后一行，答案 5，与示例 2 一致。

## 代码

`dfs` 返回 `(方案数, 子树大小)`，两个值缺一不可：没有大小就算不出 `C(ls + rs, ls)`。空树返回 `(1, 0)`，`C(0,0) = 1`，叶子因此也走通用分支，不用特判。

```python
import sys
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        sys.setrecursionlimit(max(10000, n + 100))

        class TreeNode:
            __slots__ = ("val", "left", "right")

            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        root = TreeNode(nums[0])

        def add_node(val, cur_root):
            if not cur_root:
                return TreeNode(val)
            if val < cur_root.val:
                cur_root.left = add_node(val, cur_root.left)
            else:
                cur_root.right = add_node(val, cur_root.right)
            return cur_root

        for i in range(1, n):
            add_node(nums[i], root)

        def dfs(node):
            # 返回 (方案数, 子树大小)
            if not node:
                return 1, 0
            la, ls = dfs(node.left)
            ra, rs = dfs(node.right)
            # 左右各自排好后，只需把两条序列交错：左子树挑走 ls 个空位
            return comb(ls + rs, ls) * la % MOD * ra % MOD, ls + rs + 1

        return dfs(root)[0] - 1
```

## 复杂度

- 建树：平均 `O(n log n)`，数组有序时退化为 `O(n²)`；
- 遍历计数：每个节点一次，`O(n)`；
- 空间：`O(n)` 节点 + 最坏 `O(n)` 递归栈。

`math.comb` 精确计算后取模即可。`n ≤ 1000`，不需要预处理组合数表，也不需要求逆元。

## 三个实现细节

1. `MOD` 必须写在函数最前面。Python 里函数体内有赋值就是局部变量，写在 `return` 之后会 `UnboundLocalError`。
2. `nums` 有序时树退化成链，建树和 `dfs` 的递归深度都是 `n`，默认递归限制会直接崩，要 `setrecursionlimit`。
3. 建树可改成迭代（`while` 循环往下走），链状输入下比递归 `add_node` 快约一倍，计数部分不用改。
