# [Python/Java/JavaScript/Go] DFS

> slug: pythonjavajavascriptgo-dfs-by-himymben-ctv8
> date: 2021-11-17
> tags: Go, Java, JavaScript, Python, Python3
> question: Binary Tree Tilt (binary-tree-tilt)
> url: https://leetcode.cn/problems/binary-tree-tilt/solutions/R1FHVd/pythonjavajavascriptgo-dfs-by-himymben-ctv8/

---
```Python3 []
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            l_sum, l_diff = dfs(node.left)
            r_sum, r_diff = dfs(node.right)
            return l_sum + r_sum + node.val, l_diff + r_diff + abs(r_sum - l_sum)
        return dfs(root)[1]
```
```Java []
class Solution {
    private int ans;
    public int findTilt(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode node) {
        if(node == null)
            return 0;
        int l = dfs(node.left), r = dfs(node.right);
        ans += Math.abs(r - l);
        return l + r + node.val;
    }
}
```
```JavaScript []
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findTilt = function(root) {
    let ans = 0;
    function dfs(node) {
        if(node == null)
            return 0;
        const l = dfs(node.left), r = dfs(node.right);
        ans += Math.abs(l - r);
        return node.val + l + r;
    }
    dfs(root);
    return ans;
};
```
```Go []
func findTilt(root *TreeNode) int {
    ans := 0
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if(node == nil){
            return 0
        }
        l := dfs(node.Left)
        r := dfs(node.Right)
        if v := l - r ; v > 0 {
            ans += v
        } else {
            ans -= v
        }
        return l + r + node.Val
    }
    dfs(root)
    return ans
}
```