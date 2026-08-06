# [Python/Java/JavaScript/Go] BFS通用二叉树序列化 -> 先序、后序遍历

> slug: pythonjavajavascriptgo-by-himymben-2izg
> date: 2022-05-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Serialize and Deserialize BST (serialize-and-deserialize-bst)
> url: https://leetcode.cn/problems/serialize-and-deserialize-bst/solutions/uLfsAo/pythonjavajavascriptgo-by-himymben-2izg/

---
### 解题思路
为尽量紧凑，我们用“#”表示空节点，用“,”分割节点，编码和解码中按BFS顺序排列节点。


注意上面的解法并没有利用题目的二叉搜索树的性质，我们可以利用数字大小，分割左子树与右子树。
具体来说，当我们知道根节点的值，那么所有大于根节点的，一定是右子树的一部分；其余为左子树。
后序遍历后，我们可以先得到根节点的值，根据这个值，再递归构造右子树，最后构造左子树即可。

### 代码

```Python3 [v1-BFS]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                ans.append("#")
            else:
                ans.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
        while ans and ans[-1] == '#':
            ans.pop()
        return ",".join(ans)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        strs = data.split(",")
        root = TreeNode(int(strs[0]))
        queue = deque([root])
        idx = 1
        while idx < len(strs):
            cur = queue.popleft()
            if (s:=strs[idx]) != '#':
                cur.left = TreeNode(int(s))
                queue.append(cur.left)
            idx += 1
            if idx < len(strs):
                if (s:=strs[idx]) != '#':
                    cur.right = TreeNode(int(s))
                    queue.append(cur.right)
                idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```
```Python3 [v1-后序遍历 Py]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                ans.append(str(node.val))
        dfs(root)
        return ",".join(ans)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals = list(map(int, data.split(",")))
        def dfs(left, right):
            if not vals or vals[-1] > right or vals[-1] < left:
                return None
            val = vals.pop()
            node = TreeNode(val)
            node.right = dfs(val, right)
            node.left = dfs(left, val)
            return node
        
        return dfs(-1, 1e5)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```
```Java [v1-先序遍历 Java]
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        preOrder(root, ans);
        String s = ans.toString();
        return s.substring(1, s.length() - 1);
    }

    private void preOrder(TreeNode node, List<Integer> ans) {
        if(node != null) {
            ans.add(node.val);
            preOrder(node.left, ans);
            preOrder(node.right, ans);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data == "") {
            return null;
        }
        String[] vals = data.split(", ");
        return dfs(-1, 10007, new int[]{0}, vals);
    }

    private TreeNode dfs(int left, int right, int[] idx, String[] vals) {
        if(idx[0] == vals.length)
            return null;
        int val = Integer.parseInt(vals[idx[0]]);
        if(val < left || val > right)
            return null;
        idx[0]++;
        TreeNode node = new TreeNode(val);
        node.left = dfs(left, val, idx, vals);
        node.right = dfs(val, right, idx, vals);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
```
```JavaScript [v1-后序遍历 JavaScript]
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    const ans = new Array()
    const dfs = function(node) {
        if(node != null) {
            dfs(node.left)
            dfs(node.right)
            ans.push(node.val)
        }
    }
    dfs(root)
    return ans.join(",")
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if(data == "") {
        return null
    }
    const vals = data.split(",").map(i => parseInt(i))
    const dfs = function(left, right) {
        const len = vals.length
        if(len == 0 || vals[len - 1] < left || vals[len - 1] > right)
            return null
        const val = vals.pop()
        const node = new TreeNode(val)
        node.right = dfs(val, right)
        node.left = dfs(left, val)
        return node
    }
    return dfs(-1, 10007)
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```
```Go [v1-先序遍历 Go]
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {

}

func Constructor() (_ Codec) {
    return
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    ans := []string{}
    var preOrder func(*TreeNode)
    preOrder = func(node *TreeNode) {
        if node != nil {
            ans = append(ans, strconv.Itoa(node.Val))
            preOrder(node.Left)
            preOrder(node.Right)
        }
    }
    preOrder(root)
    return strings.Join(ans, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {    
    if data == "" {
        return nil
    }
    vals := strings.Split(data, ",")
    var dfs func(left, right int) *TreeNode
    dfs = func(left, right int) *TreeNode {
        if len(vals) == 0 {
            return nil
        }
        val, _ := strconv.Atoi(vals[0])
        if val < left || val > right {
            return nil
        }
        vals = vals[1:]
        node := &TreeNode{val, nil, nil}
        node.Left = dfs(left, val)
        node.Right = dfs(val, right)
        return node
    }
    return dfs(-1, 10007)
}


/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor()
 * deser := Constructor()
 * tree := ser.serialize(root)
 * ans := deser.deserialize(tree)
 * return ans
 */
```