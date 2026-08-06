# [Python/Java/JavaScript/Go] 迭代器+双指针

> slug: pythonjavajavascriptgo-die-dai-qi-shuang-wc1k
> date: 2022-03-21
> tags: Go, Java, JavaScript, Python, Python3
> question: 两数之和 IV - 输入二叉搜索树 (opLdQZ)
> url: https://leetcode.cn/problems/opLdQZ/solutions/RWEmHq/pythonjavajavascriptgo-die-dai-qi-shuang-wc1k/

---
### 解题思路
[题解完全一致](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/solution/pythonjavajavascriptgo-by-himymben-prb2/)

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
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
            if (v := left + right) == k:
                return True
            elif v > k:
                right = next(right_gen)
            else:
                left = next(left_gen)
        return False
```