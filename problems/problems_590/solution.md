# [Python/Java/JavaScript/Go] 递归 or 迭代

> slug: -by-himymben-155v
> date: 2022-03-11
> tags: Go, Java, JavaScript, Python, Python3
> question: N-ary Tree Postorder Traversal (n-ary-tree-postorder-traversal)
> url: https://leetcode.cn/problems/n-ary-tree-postorder-traversal/solutions/mDvTto/-by-himymben-155v/

---
递归
```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            for child in node.children:
                yield from dfs(child)
            yield node.val
        
        return [v for v in dfs(root)] if root else []
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
    private List<Integer> ans;
    public List<Integer> postorder(Node root) {
        ans = new ArrayList<>();
        dfs(root);
        return ans;
    }

    private void dfs(Node node) {
        if(node != null) {
            for(Node child: node.children)
                dfs(child);
            ans.add(node.val);
        }
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
 * @return {number[]}
 */
var postorder = function(root) {
    const ans = new Array()
    dfs = function(node) {
        if(node != null) {
            for(const child of node.children)
                dfs(child)
            ans.push(node.val)
        }
    }
    dfs(root)
    return ans
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

func postorder(root *Node) (ans []int) {
    var dfs func(node *Node)
    dfs = func(node *Node) {
        if node != nil {
            for _, child := range node.Children {
                dfs(child)
            }
            ans = append(ans, node.Val)
        }
    }
    dfs(root)
    return
}
```

迭代
```Python3 []
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, ans = [root], []
        while stack:
            if (obj := stack.pop()) is not None:
                if type(obj) == Node:
                    stack += [obj.val] + obj.children[::-1]
                else:
                    ans.append(obj)
        return ans
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
    public List<Integer> postorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if(root != null) {
            Deque<Object> stack = new ArrayDeque<>();
            stack.addLast(root);
            while(!stack.isEmpty()) {
                Object obj = stack.pollLast();
                if(obj instanceof Node) {
                    Node node = (Node)obj;
                    stack.addLast(new Integer(node.val));
                    for(int i = node.children.size() - 1; i >= 0; i--)
                        stack.addLast(node.children.get(i));
                } else
                    ans.add((Integer)obj);
            }
        }
        return ans;
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
 * @return {number[]}
 */
var postorder = function(root) {
    if(root == null)
        return []
    const stack = [root], ans = new Array()
    while(stack.length > 0) {
        const obj = stack.pop()
        if(obj instanceof Node) {
            stack.push(obj.val)
            for(let i = obj.children.length - 1; i >= 0; i--)
                stack.push(obj.children[i])
        } else
            ans.push(obj)
    }
    return ans
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

func postorder(root *Node) (ans []int) {
    if root == nil {
        return
    }
    stack := []interface{}{root}
    for l := len(stack); l > 0; l = len(stack) {
        obj := stack[l - 1]
        stack = stack[:l - 1]
        if value, ok := obj.(int); ok {
            ans = append(ans, value)
        } else {
            value, _ := obj.(*Node)
            stack = append(stack, value.Val)
            for i := len(value.Children) - 1; i >= 0; i-- {
                stack = append(stack, value.Children[i])
            }
        }
    }
    return
}
```