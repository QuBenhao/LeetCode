# [Python/Java/JavaScript/Go] BFS

> slug: pythonjavajavascriptgo-bfs-by-himymben-qn71
> date: 2021-12-24
> tags: Go, Java, JavaScript, Python, Python3
> question: Even Odd Tree (even-odd-tree)
> url: https://leetcode.cn/problems/even-odd-tree/solutions/58krid/pythonjavajavascriptgo-bfs-by-himymben-qn71/

---
### 解题思路
BFS可以保证维护当前层数，以及从左到右的判断顺序，很适合本题。
只要依次判断每层是否满足奇偶树，不满足的话直接返回False即可。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level, nodes = 0, [root]
        while nodes:
            nxt, cur = [], inf if level % 2 else 0
            for node in nodes:
                if (level % 2 == node.val % 2) or (level % 2 and cur <= node.val) or ((not level % 2) and cur >= node.val):
                        return False
                cur = node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            nodes = nxt
            level += 1
        return True
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
    public boolean isEvenOddTree(TreeNode root) {
        int level = 0;
        List<TreeNode> nodes = new ArrayList<>(){{add(root);}};
        while(nodes.size()>0){
            List<TreeNode> nxt = new ArrayList<>();
            int cur = level % 2 != 0 ? 1000001 : 0;
            for(TreeNode node: nodes) {
                if(level % 2 == node.val % 2 || (level % 2 == 0 && cur >= node.val) || (level % 2 != 0 && cur <= node.val))
                    return false;
                cur = node.val;
                if(node.left != null)
                    nxt.add(node.left);
                if(node.right != null)
                    nxt.add(node.right);
            }
            nodes = nxt;
            level++;
        }
        return true;
    }
}
```
```JavaScript []
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
 * @return {boolean}
 */
var isEvenOddTree = function(root) {
    let nodes = [root], level = 0
    while(nodes.length > 0){
        const nxt = new Array()
        let cur = level % 2 == 0 ? 0 : 1000001
        for(const node of nodes){
            if(level % 2 == node.val % 2 || (level % 2 == 0 && cur >= node.val) || (level % 2 != 0 && cur <= node.val))
                return false
            cur = node .val
            if(node.left != null)
                nxt.push(node.left)
            if(node.right != null)
                nxt.push(node.right)
        }
        nodes = nxt
        level++
    }
    return true
};
```
```Go []
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isEvenOddTree(root *TreeNode) bool {
    nodes, level := []*TreeNode{root}, 0
    for len(nodes) > 0 {
        length, cur := len(nodes), 0
        if level % 2 == 1{
            cur = 1000001
        }
        for i:=0;i<length;i++ {
            node := nodes[0]
            nodes = nodes[1:]
            if level % 2 == node.Val % 2 || (level % 2 == 0 && cur >= node.Val) || (level % 2 != 0 && cur <= node.Val){
                return false
            }
            cur = node.Val
            if node.Left != nil{
                nodes = append(nodes, node.Left)
            }
            if node.Right != nil{
                nodes = append(nodes, node.Right)
            }
        }
        level++
    }
    return true
}
```