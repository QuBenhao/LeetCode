# [Python/Java/TypeScript/Go] 递归

> slug: pythonjavatypescriptgo-di-gui-by-himymbe-ltm8
> date: 2022-07-15
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Logical OR of Two Binary Grids Represented as Quad-Trees (logical-or-of-two-binary-grids-represented-as-quad-trees)
> url: https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/solutions/HDSLTB/pythonjavatypescriptgo-di-gui-by-himymbe-ltm8/

---
### 解题思路
本题和[427](https://leetcode.cn/problems/construct-quad-tree/solution/python-by-himymben-ld18/)没有什么区别，
由于是或运算，所以很多时候我们不需要递归到最深，当有一个是叶子节点后，它如果是1那么或结果必然是1，如果是0那么或结果必然是另一个节点。
注意将结果一致的四个子节点合并为一个新的叶子节点即可。

### 代码

```Python3 []
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree2.val else quadTree1
        tl, tr, bl, br = self.intersect(quadTree1.topLeft, quadTree2.topLeft), self.intersect(quadTree1.topRight, quadTree2.topRight), self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        return Node(tl.val, True, None, None, None, None) if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val else Node(False, False, tl, tr, bl, br)
```
```Java []
/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
    public Node intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1.isLeaf) {
            return quadTree1.val ? new Node(true, true, null, null, null, null) : quadTree2;
        }
        if (quadTree2.isLeaf) {
            return quadTree2.val ? new Node(true, true, null, null, null, null) : quadTree1;
        }
        Node tl = intersect(quadTree1.topLeft, quadTree2.topLeft), tr = intersect(quadTree1.topRight, quadTree2.topRight), bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), br = intersect(quadTree1.bottomRight, quadTree2.bottomRight);
        return tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf && tl.val == tr.val && tl.val == bl.val && tl.val == br.val ? new Node(tl.val, true, null, null, null, null) : new Node(false, false, tl, tr, bl, br);
    }
}
```
```TypeScript []
/**
 * Definition for node.
 * class Node {
 *     val: boolean
 *     isLeaf: boolean
 *     topLeft: Node | null
 *     topRight: Node | null
 *     bottomLeft: Node | null
 *     bottomRight: Node | null
 *     constructor(val?: boolean, isLeaf?: boolean, topLeft?: Node, topRight?: Node, bottomLeft?: Node, bottomRight?: Node) {
 *         this.val = (val===undefined ? false : val)
 *         this.isLeaf = (isLeaf===undefined ? false : isLeaf)
 *         this.topLeft = (topLeft===undefined ? null : topLeft)
 *         this.topRight = (topRight===undefined ? null : topRight)
 *         this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
 *         this.bottomRight = (bottomRight===undefined ? null : bottomRight)
 *     }
 * }
 */

function intersect(quadTree1: Node | null, quadTree2: Node | null): Node | null {
    if (quadTree1.isLeaf) {
        return quadTree1.val ? new Node(true, true, null, null, null, null) : quadTree2
    }
    if (quadTree2.isLeaf) {
        return quadTree2.val ? new Node(true, true, null, null, null, null) : quadTree1
    }
    const tl: Node = intersect(quadTree1.topLeft, quadTree2.topLeft), tr = intersect(quadTree1.topRight, quadTree2.topRight), bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
    return tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf && tl.val == tr.val && tl.val == bl.val && tl.val == br.val ? new Node(tl.val, true, null, null, null, null) : new Node(false, false, tl, tr, bl, br)
};
```
```Go []
/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func intersect(quadTree1 *Node, quadTree2 *Node) *Node {
    if quadTree1.IsLeaf {
        if quadTree1.Val {
            return &Node{true, true, nil, nil, nil, nil}
        }
        return quadTree2
    }
    if quadTree2.IsLeaf {
        if quadTree2.Val {
            return &Node{true, true, nil, nil, nil, nil}
        }
        return quadTree1
    }
    tl, tr, bl, br := intersect(quadTree1.TopLeft, quadTree2.TopLeft), intersect(quadTree1.TopRight, quadTree2.TopRight), intersect(quadTree1.BottomLeft, quadTree2.BottomLeft), intersect(quadTree1.BottomRight, quadTree2.BottomRight)
    if tl.IsLeaf && tr.IsLeaf && bl.IsLeaf && br.IsLeaf && tl.Val == tr.Val && tl.Val == bl.Val && tl.Val == br.Val {
        return &Node{tl.Val, true, nil, nil, nil, nil}
    }
    return &Node{false, false, tl, tr, bl, br}
}
```