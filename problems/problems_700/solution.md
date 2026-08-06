# [Python/Java/JavaScript/Go] 递归

> slug: pythonjavajavascriptgo-di-gui-by-himymbe-stvf
> date: 2021-11-25
> tags: Go, Java, JavaScript, Python, Python3
> question: Search in a Binary Search Tree (search-in-a-binary-search-tree)
> url: https://leetcode.cn/problems/search-in-a-binary-search-tree/solutions/uJ3GPE/pythonjavajavascriptgo-di-gui-by-himymbe-stvf/

---
```Python3 []
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return root if not root or root.val == val else (self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val))
```
```Java []
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null || root.val == val)
            return root;
        return root.val > val ? searchBST(root.left, val) : searchBST(root.right, val);
    }
}
```
```JavaScript []
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    if(root == null || root.val == val)
        return root
    return root.val > val ? searchBST(root.left, val) : searchBST(root.right, val)
};
```
```Go []
func searchBST(root *TreeNode, val int) *TreeNode {
    if(root == nil || root.Val == val) {
        return root
    }
    if(root.Val > val){
        return searchBST(root.Left, val)
    } else {
        return searchBST(root.Right, val)
    }
}
```