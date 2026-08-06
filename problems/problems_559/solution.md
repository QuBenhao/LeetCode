# [Python/Java/JavaScript/Go] 递归

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-lu2y
> date: 2021-11-20
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Depth of N-ary Tree (maximum-depth-of-n-ary-tree)
> url: https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/solutions/E1jk9d/pythonjavajavascriptgo-di-gui-by-himymbe-lu2y/

---
### 解题思路
每个节点的最大深度由它所有子节点的最大深度的最大值的决定

### 代码

```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return max(self.maxDepth(child) for child in root.children) + 1 if root and root.children else int(root != None)
```
```Java []
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        if(root == null)
            return 0;
        int ans = 0;
        for(Node child: root.children)
            ans = Math.max(ans, maxDepth(child));
        return ans + 1;
    }
}
```
```JavaScript []
/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number}
 */
var maxDepth = function(root) {
    if(root == null)
        return 0;
    let ans = 0;
    for(const child of root.children)
        ans = Math.max(ans, maxDepth(child));
    return ans + 1;
};
```
```Go []
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func maxDepth(root *Node) int {
    if root == nil {
        return 0
    }
    ans := 0
    for _, child := range root.Children {
        v := maxDepth(child)
        if v > ans {
            ans = v
        }
    }
    return ans + 1
}

```