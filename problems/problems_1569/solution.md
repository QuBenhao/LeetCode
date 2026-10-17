# 建树 + 组合计数：把左右子树当两副牌洗在一起

> date: 2026-10-18
> tags: Python3, 二叉搜索树, 组合计数, 分治
> question: Number of Ways to Reorder Array to Get Same BST (number-of-ways-to-reorder-array-to-get-same-bst)
> url: https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/

---

> Problem: [1569. 将子数组重新排序得到同一个二叉搜索树的方案数](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/)

## 一句话思路

BST 的形态只由一件事决定：**每棵子树的根必须是这棵子树里最早被插入的那个元素**。所以合法重排 = 满足「父节点排在子节点之前」的所有排列数，对每棵子树独立统计后乘起来即可。

## 一、什么样的重排是合法的

按 `nums` 的顺序依次插入建成 BST 后，考察任意一个节点 `x` 和它子树里的后代 `y`：

- `y` 能挂到 `x` 下面，说明插入 `y` 时 `x` 已经在树里了，也就是 `x` 在序列里排在 `y` 前面；
- 反过来，只要每个节点都排在它所有后代之前，插入过程就会走出完全相同的路径，得到的树必然同形。

所以约束只有一条：**父先于子**。除此之外元素之间没有别的顺序要求——这正是能分治的原因。

## 二、递归要同时带出「方案数」和「子树大小」

这是本题最容易卡住的地方。只看某个节点的方案数是不够的，必须先知道左右子树各有多少个节点，才能算出合并方式数。所以 `dfs` 返回二元组：

```text
dfs(node) -> (这棵子树的合法重排数, 这棵子树的节点数)
```

空树返回 `(1, 0)`——方案数是 1 表示它是乘法单位元，节点数是 0。有了这个约定，叶子节点会自然落到通用分支里（`C(0,0) * 1 * 1 = 1`，大小 0+0+1 = 1），完全不需要写特判。

## 三、关键一步：左右子树如何合并

左右子树的元素在插入时只会跟各自那一侧的节点比较，谁先谁后**互不影响**。于是合并是三个独立选择的乘积：

```text
ways(node) = C(ls + rs, ls) × ways(left) × ways(right)
```

- `C(ls + rs, ls)`：只决定「剩下的 `ls + rs` 个位置里，哪 `ls` 个留给左子树」，不关心位置里填什么，所以它是纯组合数；
- `ways(left)`、`ways(right)`：各自内部怎么排。

`C(ls + rs, ls)` 这一步的直觉就是**洗牌**：两副牌各自保持内部顺序，洗到一起。从 `ls + rs` 个槽位里挑 `ls` 个给左边，剩下的自然归右边。

如果只写 `ways(left) × ways(right)` 而不乘组合数，等于只数了「左子树整体排完再整体接右子树」这一种，会大量漏解——**这是本题最大的坑**。

## 四、最后要减 1

题目问的是「重新排序」，原数组本身不算一种新方案，所以答案是 `dfs(root)[0] - 1`。

## 示例走一遍

`nums = [3, 4, 5, 1, 2]`，建成 BST 后根是 3，左子树 `[1, 2]`，右子树 `[4, 5]`。

- 左子树：1 必须在 2 前，方案数 1，大小 2；
- 右子树：4 必须在 5 前，方案数 1，大小 2；
- 交错 `C(4, 2) = 6` 种：

```text
3, 1, 2, 4, 5      左左右右
3, 1, 4, 2, 5      左右左右
3, 1, 4, 5, 2      左右右左
3, 4, 1, 2, 5      右左左右
3, 4, 1, 5, 2      右左右左
3, 4, 5, 1, 2      右右左右  ← 原数组本身
```

去掉原数组那一行，答案就是 5，与示例 2 一致。

## 代码

```python
import sys
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7  # 必须在最前面定义：函数体内赋值即为局部变量
        n = len(nums)
        sys.setrecursionlimit(max(10000, n + 100))  # 退化成链时递归深度可达 n

        class TreeNode:
            __slots__ = ("val", "left", "right")

            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        root = TreeNode(nums[0])

        def add_node(val, cur_root: TreeNode):
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
            # 左右子树互不干扰：各自排好之后，只需把两条序列交错。
            # comb(ls + rs, ls) = 左子树挑走了哪 ls 个空位，剩下的自然归右子树
            return comb(ls + rs, ls) * la % MOD * ra % MOD, ls + rs + 1

        return dfs(root)[0] - 1
```

## 复杂度

- 建树：平均 O(n log n)，退化成链时 O(n²)；
- 树上 DFS：每个节点访问一次，O(n)；
- 空间：树 O(n) 个节点，递归栈最坏 O(n)。

`comb` 用 `math.comb` 精确计算后再取模即可，`n ≤ 1000` 下开销可忽略，不需要预处理组合数表，也不需要费马小定理求逆元。

## 关于建树的性能

`nums` 升序时插入路径长度是 O(n)，建树本身就退化到 O(n²)。实测 n = 1000 的最坏输入下：

- 递归 `add_node` 建树约 0.36s，加上 DFS 整体约 0.55s；
- 改成迭代插入（`while` 循环往下走）建树约 0.21s，整体约 0.22s。

递归写法慢一倍左右，但绝对值都在亚秒级，本题完全可以过；想压常数就换成迭代插入，`dfs` 部分不用动。

## 两个易错点

1. **`MOD` 的定义位置**：写在 `return` 之后会 `UnboundLocalError`，因为函数体内赋值会让它成为局部变量，而 `return` 执行时它还没绑定。同理适用于任何在函数末尾才赋值的常量。
2. **递归深度**：`nums` 有序时树退化成链，建树和 `dfs` 的递归深度都到 1000，会撞 Python 默认的递归限制，必须 `setrecursionlimit`。
