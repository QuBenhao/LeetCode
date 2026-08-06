# [Python3/Java/TypeScript/Go/C/C++/C#/Js/PHP/Python] 递归

> slug: pythonjavatypescriptgo-di-gui-by-himymbe-m57o
> date: 2022-08-29
> tags: C, C++, C#, Go, Java, JavaScript, PHP, Python, Python3, TypeScript
> question: Maximum Binary Tree II (maximum-binary-tree-ii)
> url: https://leetcode.cn/problems/maximum-binary-tree-ii/solutions/8CgAt1/pythonjavatypescriptgo-di-gui-by-himymbe-m57o/

---
### 解题思路
因为是在数组末尾添加新的val，所以我们可以和根节点比较，
如果比根节点大，那么说明val是新的根且原根节点是其左子树(因为val在数组中是原根的值的右边)。
如果比根节点小，那么说明val必然是递归添加在原根右节点中。注意递归时可能会改变右子树的根，所以重新赋值根节点的右节点即可。
最后如果递归到根为空，直接返回一个新叶子节点既可。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val < val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
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
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (root == null || root.val < val) {
            return new TreeNode(val, root, null);
        }
        root.right = insertIntoMaxTree(root.right, val);
        return root;
    }
}
```
```TypeScript []
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function insertIntoMaxTree(root: TreeNode | null, val: number): TreeNode | null {
    if (root == null || root.val < val) {
        return new TreeNode(val, root)
    }
    root.right = insertIntoMaxTree(root.right, val)
    return root
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
func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
    if root == nil || root.Val < val {
        return &TreeNode{val, root, nil}
    }
    root.Right = insertIntoMaxTree(root.Right, val)
    return root
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
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoMaxTree = function(root, val) {
    if (root == null || root.val < val) {
        return new TreeNode(val, root, null)
    }
    root.right = insertIntoMaxTree(root.right, val)
    return root
};
```
```C++ []
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        if (root == nullptr || root->val < val) {
            return new TreeNode(val, root, nullptr);
        }
        root->right = insertIntoMaxTree(root->right, val);
        return root;
    }
};
```
```C []
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* creatTreeNode(int val, const struct TreeNode *left, const struct TreeNode *right) {
    struct TreeNode* node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = left;
    node->right = right;
    return node;
}

struct TreeNode* insertIntoMaxTree(struct TreeNode* root, int val){
    if (root == NULL || root->val < val) {
        return creatTreeNode(val, root, NULL);
    }
    root->right = insertIntoMaxTree(root->right, val);
    return root;
}
```
```C# []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode InsertIntoMaxTree(TreeNode root, int val) {
        if (root == null || root.val < val) {
            return new TreeNode(val, root);
        }
        root.right = InsertIntoMaxTree(root.right, val);
        return root;
    }
}
```
```PHP []
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @param Integer $val
     * @return TreeNode
     */
    function insertIntoMaxTree($root, $val) {
        if ($root == null || $root->val < $val) {
            return new TreeNode($val, $root);
        }
        $root->right = $this->insertIntoMaxTree($root->right,$val);
        return $root;
    }
}
```
```Python []
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val < val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
```